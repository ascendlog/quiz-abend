#!/usr/bin/env python3
"""Erzeugt die aufgenommenen Vorlese-Clips (audio/<hash>.mp3 + audio/index.json).

Stimme: Piper „thorsten“ (medium, CC0), Phonemisierung mit espeak-ng.
Benötigt: onnxruntime, numpy, scipy, ffmpeg, das Modell (vits-piper-de_DE-thorsten-medium von
https://github.com/k2-fsa/sherpa-onnx/releases/tag/tts-models) und ein gebautes espeak-ng.
Aufruf:  MODEL_DIR=... ESPEAK=... python3 tools/make_audio.py [--force]
Die Dateinamen sind ein Hash des gesprochenen Textes. Dieselbe Regel steckt in index.html (hashText und
die Teile in fQParts/fFbParts). Wer Texte ändert, erzeugt nur die neuen Clips; alte Hashes fallen aus dem Index.
"""
import json, os, re, subprocess, sys, unicodedata
from multiprocessing import Pool

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.environ.get('MODEL_DIR', '/tmp/tts/vits-piper-de_DE-thorsten-medium')
ESPEAK = os.environ.get('ESPEAK', '/tmp/tts/espeak-ng/build/src/espeak-ng')
OUT = os.path.join(ROOT, 'audio')
LENGTH_SCALE, NOISE_SCALE, NOISE_W = 1.08, 0.6, 0.75
SENTENCE_PAUSE, TAIL = 0.28, 0.35
VOICE_SAMPLE = 'Hallo! Ich lese euch die Fragen vor. Welches Tier sagt Miau?'


def plain(t):
    t = re.sub('[\U0001F000-\U0001FAFF←-⯿️‍]', ' ', str(t))
    return re.sub(r'\s+', ' ', t).strip()


def hash_text(t):
    h1, h2 = 0x811c9dc5, 5381
    b = t.encode('utf-16-le')
    for i in range(0, len(b), 2):
        c = b[i] | (b[i + 1] << 8)
        h1 = ((h1 ^ c) * 16777619) & 0xffffffff
        h2 = (h2 * 33 + c) & 0xffffffff
    return '%08x%08x' % (h1, h2)


def end_dot(t):
    return t if re.search(r'[.!?…]$', t) else t + '.'


def collect():
    texts = set()

    def add(t):
        t = plain(t)
        if t:
            texts.add(t)

    for L in 'ABCD':
        add('Antwort %s.' % L)
    for t in ['Wahr oder falsch?', 'Wahr.', 'Falsch.', 'Geschafft! Super.', 'Nächstes Mal klappt es.',
              'Stimmt!', 'Stimmt nicht.', 'Richtig!', 'Nicht ganz. Richtig ist:', VOICE_SAMPLE]:
        add(t)

    def item(q):
        add(q['frage'])
        if q['typ'] == 'mc':
            for a in q['antworten']:
                add(end_dot(plain(a)))
        if q.get('info'):
            add(q['info'])

    fam = json.load(open(os.path.join(ROOT, 'familienfragen.json'), encoding='utf-8'))['fragen']
    for q in fam:
        if q['typ'] != 'fam':          # Familienfragen enthalten Namen -> iPhone-Stimme
            item(q)
    wis = json.load(open(os.path.join(ROOT, 'fragen.json'), encoding='utf-8'))['fragen']
    for q in wis:
        if q['typ'] in ('mc', 'tf') and q.get('thema') != 'psychologie' and q['stufe'] <= 2:
            item(q)
    bad = [t for t in texts if '{' in t or '}' in t]
    assert not bad, bad
    return sorted(texts)


# ── Synthese (pro Prozess einmal geladen) ───────────────────────────────────
_S = {}


def _init():
    import numpy as np, onnxruntime as ort
    cfg = json.load(open(MODEL_DIR + '/de_DE-thorsten-medium.onnx.json'))
    so = ort.SessionOptions(); so.intra_op_num_threads = 1
    _S.update(np=np, cfg=cfg, idm=cfg['phoneme_id_map'], sr=cfg['audio']['sample_rate'],
              sess=ort.InferenceSession(MODEL_DIR + '/de_DE-thorsten-medium.onnx', so, providers=['CPUExecutionProvider']))


def _phon(clause):
    out = subprocess.run([ESPEAK, '--path=' + MODEL_DIR, '-v', 'de', '-q', '--ipa', clause], capture_output=True, text=True).stdout
    return ' '.join(l.strip() for l in out.splitlines() if l.strip())


def _ids(ph):
    idm = _S['idm']
    ids = list(idm['^'])
    for ch in unicodedata.normalize('NFD', ph):
        if ch in idm:
            ids += idm[ch] + idm['_']
    return ids + idm['$']


def _sentence(s):
    np = _S['np']
    ph = ''
    for p in re.findall(r'[^,;:.!?]+[,;:.!?]?', s):
        p = p.strip()
        if not p:
            continue
        punct = p[-1] if p[-1] in ',;:.!?' else ''
        body = p[:-1] if punct else p
        ph += (_phon(body) if re.search(r'\w', body) else '') + punct + ' '
    ids = np.array([_ids(ph.strip())], dtype=np.int64)
    feeds = {'input': ids, 'input_lengths': np.array([ids.shape[1]], dtype=np.int64),
             'scales': np.array([NOISE_SCALE, LENGTH_SCALE, NOISE_W], dtype=np.float32)}
    return _S['sess'].run(None, feeds)[0].squeeze().astype(np.float32)


def render(text):
    np, sr = _S['np'], _S['sr']
    segs = []
    for s in re.findall(r'[^.!?]+[.!?]?', text):
        if re.search(r'\w', s):
            segs += [_sentence(s.strip()), np.zeros(int(sr * SENTENCE_PAUSE), dtype=np.float32)]
    a = np.concatenate(segs[:-1])                       # letzte Pause weg, Ende kommt unten
    rms = float(np.sqrt(np.mean(a ** 2))) or 1e-6
    a = a * (0.09 / rms)                                # gleiche Lautheit für kurze und lange Clips
    peak = float(np.abs(a).max())
    if peak > 0.95:
        a = a * (0.95 / peak)
    a = np.concatenate([a, np.zeros(int(sr * TAIL), dtype=np.float32)])
    return (a * 32767).astype(np.int16).tobytes(), sr


def work(text):
    h = hash_text(text)
    path = os.path.join(OUT, h + '.mp3')
    if os.path.exists(path) and '--force' not in sys.argv:
        return h, text, 'vorhanden'
    if not _S:
        _init()
    pcm, sr = render(text)
    r = subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 's16le', '-ar', str(sr), '-ac', '1', '-i', '-',
                        '-codec:a', 'libmp3lame', '-b:a', '40k', path], input=pcm, capture_output=True)
    if r.returncode:
        raise RuntimeError(r.stderr.decode())
    return h, text, 'neu'


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    texts = collect()
    print(len(texts), 'Texte')
    done, neu = {}, 0
    with Pool(int(os.environ.get('JOBS', '4')), initializer=_init) as pool:
        for i, (h, t, st) in enumerate(pool.imap_unordered(work, texts, chunksize=4)):
            done[h] = t
            neu += st == 'neu'
            if (i + 1) % 50 == 0:
                print(i + 1, '/', len(texts), flush=True)
    assert len(done) == len(texts), 'Hash-Kollision'
    # verwaiste Clips entfernen
    for f in os.listdir(OUT):
        if f.endswith('.mp3') and f[:-4] not in done:
            os.remove(os.path.join(OUT, f))
    json.dump({'v': 1, 'voice': 'Piper thorsten (medium)', 'clips': sorted(done)},
              open(os.path.join(OUT, 'index.json'), 'w'), separators=(',', ':'))
    print('fertig:', neu, 'neu,', len(done), 'insgesamt')

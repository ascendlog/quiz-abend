# Quiz-Abend

Quizspiel für zwei – gedacht für einen Spieleabend zu zweit, läuft als Web-App auf dem iPhone (Home-Bildschirm).

## Dateien

- `index.html` – das Spiel: Wissensspiel auf einem Handy (abwechselnd) oder auf zwei Handys (gleichzeitig, live)
- `fragen.json` – Fragenpaket (102 Fragen: Geografie, Geschichte, Natur & Wissenschaft inkl. Psychologie, Kultur, Sport, Mode)
- `verbindungstest.html` – Diagnose-Seite: prüft, ob sich zwei iPhones im WLAN direkt verbinden
- `icon.png` – Symbol für den Home-Bildschirm

## Spielregeln

- Fragetypen: Multiple Choice, Wahr/Falsch, Schätzfragen
- 10 Punkte pro richtige Antwort, bis zu 5 Zeitbonus-Punkte (20 s bei Auswahlfragen)
- Schätzfragen: Wer näher dran liegt, bekommt 10 Punkte, ein exakter Treffer gibt +5 (30 s)
- Joker pro Person: 1× 50:50, 1× Frage tauschen
- Spielende wählbar: feste Anzahl Fragen oder Zielpunkte

## Zwei Handys (live)

- Handy 1: „Zwei Handys“ → Name → „Raum erstellen“ → Einstellungen wählen → vierstelliger Code erscheint.
- Handy 2: „Zwei Handys“ → Name → Code eingeben → „Beitreten“. Dann startet Handy 1 das Spiel.
- Beide sehen dieselbe Frage und antworten gleichzeitig; der Zeitbonus zählt für jede Person einzeln.
- 50:50 ist privat (nur auf dem eigenen Handy), „Tauschen“ wechselt die Frage für beide und geht nur, solange noch niemand geantwortet hat.
- Bricht eine Verbindung ab (z. B. Sperrbildschirm), pausiert die Frage und läuft nach dem automatischen Wiederverbinden weiter.
- Handy 1 hält den Spielstand. Lädt Handy 1 neu, kann es über „Fortsetzen“ den Raum mit demselben Code wieder öffnen.
- Verbindung: direkt zwischen den Handys (WebRTC), vermittelt über den öffentlichen PeerJS-Server. Nur die Bibliothek wird von dort geladen, Fragen und Antworten laufen nicht über einen Server.

## Eigene Fragen

Über „Importieren“ auf dem Startbildschirm lassen sich weitere Fragen als JSON-Datei laden. Sie bleiben nur lokal im Browser des Handys gespeichert (nicht im öffentlichen Repo). Im Zwei-Handy-Modus zählen die Fragen von Handy 1. Format wie in `fragen.json`. „Sichern“ exportiert importierte Fragen und die Bilanz.

## Hinweis zum Speicher

Safari und die Home-Bildschirm-App haben getrennten Speicher. Am besten immer nur über das Home-Bildschirm-Symbol spielen und gelegentlich „Sichern“ nutzen.

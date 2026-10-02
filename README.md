# Quiz-Abend

Quizspiel für zwei – gedacht für einen Spieleabend zu zweit, läuft als Web-App auf dem iPhone (Home-Bildschirm).

## Dateien

- `index.html` – die App: Wissensspiel „Wer weiß mehr?“ (ein Handy abwechselnd oder zwei Handys live), der „Paarabend“ (zwei Handys) und die „Familienrunde“ (ein Handy für alle)
- `fragen.json` – Fragenpaket (102 Fragen: Geografie, Geschichte, Natur & Wissenschaft inkl. Psychologie, Kultur, Sport, Mode)
- `paarfragen.json` – Vorschläge für den Paarabend (64 Fragen in drei Stufen, Freitext oder Auswahl)
- `familienfragen.json` – Fragen für die Familienrunde (163 Fragen in drei Altersstufen: Auswahl, Wahr/Falsch, Mitmach-Aufgaben, Familienfragen)
- `verbindungstest.html` – Diagnose-Seite: prüft, ob sich zwei iPhones im WLAN direkt verbinden
- `icon.png` – Symbol für den Home-Bildschirm

## Spielregeln

- Fragetypen: Multiple Choice, Wahr/Falsch, Schätzfragen
- 10 Punkte pro richtige Antwort, bis zu 5 Zeitbonus-Punkte (30 s pro Frage)
- Schätzfragen: Wer näher dran liegt, bekommt 10 Punkte, ein exakter Treffer gibt +5
- Joker pro Person: 1× 50:50, 1× Frage tauschen
- Spielende wählbar: feste Anzahl Fragen oder Zielpunkte

## Zwei Handys (live)

- Handy 1: „Zwei Handys“ → Name → „Raum erstellen“ → Einstellungen wählen → vierstelliger Code erscheint.
- Handy 2: „Zwei Handys“ → Name → Code eingeben → „Beitreten“. Dann startet Handy 1 das Spiel.
- Beide sehen dieselbe Frage und antworten gleichzeitig; der Zeitbonus zählt für jede Person einzeln.
- 50:50 ist privat (nur auf dem eigenen Handy), „Tauschen“ wechselt die Frage für beide und geht nur, solange noch niemand geantwortet hat.
- Bricht eine Verbindung ab (z. B. Sperrbildschirm), pausiert die Frage und läuft nach dem automatischen Wiederverbinden weiter. Das dauert meist 2 bis 6 Sekunden: Beim Entsperren prüft die App die Verbindung sofort, nach langer Pause baut sie direkt neu auf. Öffnet Handy 2 die App neu und tritt mit demselben Namen wieder bei, übernimmt Handy 1 die neue Verbindung sofort. Ein anderer Name bekommt weiter „Raum belegt“.
- Findet Handy 2 den Raum nicht (z. B. weil Handy 1 noch neu lädt), fragt es zuerst alle 1,5 Sekunden, später alle 3 Sekunden nach, insgesamt gut eine Minute lang.
- Handy 1 hält den Spielstand. Lädt Handy 1 neu, kann es über „Fortsetzen“ den Raum mit demselben Code wieder öffnen.
- Verbindung: direkt zwischen den Handys (WebRTC), vermittelt über den öffentlichen PeerJS-Server. Nur die Bibliothek wird von dort geladen, Fragen und Antworten laufen nicht über einen Server.

## Paarabend (zwei Handys)

Fragen über euch beide, ohne Zeitdruck. Start: „Paarabend – zwei Handys“, Verbindung wie beim Live-Spiel (Handy 1 erstellt den Raum, Handy 2 gibt den Code ein).

- Spielart „Kennst du mich?“: Beide beantworten die Frage für sich (privat), dann rät jede Person, was der andere geantwortet hat. Freitext-Tipps bewertet die Person, um die es geht („Treffer“ 10 Punkte, „Fast“ 5, „Daneben“ 0). Auswahlfragen werden automatisch bewertet.
- Spielart „Wie ähnlich sind wir?“: Beide antworten für sich, danach seht ihr, wo ihr gleich geantwortet habt. Bei Freitext müssen beide „Gleich“ wählen.
- Tiefe: Leicht (Vorlieben, Alltag), Persönlich (Erinnerungen, ihr beide), Tief (Wünsche, Werte, Nähe) oder Gemischt (von leicht bis tief).
- Wertung: „Gegeneinander“ (Punkte, einer liegt vorn) oder „Gemeinsam“ (alle Treffer zählen zusammen). Bei „Tief“ ist „Gemeinsam“ voreingestellt.
- Jede Frage lässt sich überspringen. Am Ende gibt es Impulse zum Weiterreden und einen Rückblick mit allen Antworten.
- Es zählt immer die Fragenliste von Handy 1. Der Paarabend fließt nicht in die Bilanz des Wissensspiels ein.
- Eigene Paarfragen („Eigene Paarfragen“ auf dem Startbildschirm): Freitext oder Auswahl, mit Stufe. Sie bleiben nur lokal auf dem Handy und werden nicht ins Repo geschrieben. Import ebenfalls über „Importieren“ (JSON mit `paarfragen`-Liste im Format von `paarfragen.json`), Die Sicherung enthält sie ebenfalls.

## Pause und Fortsetzen

Gilt für den Paarabend und das Zwei-Handy-Spiel, zum Beispiel wenn ein Kind aufwacht.

- Oben rechts „Beenden“ tippen → „Pause machen“. Beide Handys landen auf dem Startbildschirm, der Stand bleibt gespeichert (auch beim Schließen der App). Es spielt keine Rolle, wer die Pause macht.
- Weitermachen: Zuerst tippt Handy 1 auf der Startseite bei der Karte „… pausiert“ auf „Fortsetzen“. Danach tippt Handy 2 bei seiner Karte auf „Fortsetzen“ und verbindet sich automatisch. Ihr landet genau in der Frage, in der ihr aufgehört habt, bereits gegebene Antworten bleiben erhalten.
- Tippt Handy 2 zu früh, sucht es einfach weiter, bis Handy 1 den Raum geöffnet hat (nach gut einer Minute ggf. noch einmal „Fortsetzen“ tippen).
- „Verwerfen“ an der Karte löscht den pausierten Abend auf dem jeweiligen Handy. „Spiel beenden“ im Pause-Dialog beendet den Abend ohne Pause. Wer einen neuen Raum erstellt, während ein Abend pausiert ist, wird vorher gefragt.
- In der Wartehalle und am Ende gibt es keinen Pause-Dialog, dort reicht „Raum schließen“ / „Verlassen“ bzw. „Zum Start“.

## Familienrunde (ein Handy für alle)

Startseite → „Familienrunde starten“. Gedacht für 2 bis 6 Personen an einem Handy, auch mit Kindern, die noch kein eigenes Handy haben.

- Einrichten: Namen eintragen und je Person eine Altersstufe wählen (Klein bis ca. 6 Jahre, Mittel 7 bis 9, Groß 10 bis 12, Erwachsen ab 13). Namen und Einstellungen bleiben nur auf diesem Handy, nicht im Repo.
- Ablauf: Die Personen sind reihum dran. Der Bildschirm sagt, wer als Nächstes dran ist, erst dann kommt „Frage zeigen“. Wer noch nicht lesen kann, bekommt die Frage vorgelesen, die Antwort tippt, wer das Handy hält. Es gibt keinen Zeitdruck.
- Jede Person bekommt Fragen passend zur Stufe. Klein und Mittel nutzen nur die Familienfragen, Groß und Erwachsen zusätzlich leichte bis mittlere Wissensfragen (ohne Psychologie). Die Fragenarten sind Auswahl, Wahr/Falsch, Mitmach-Aufgaben („Hüpfe dreimal wie ein Hase.“) und Familienfragen („Was isst Anna am liebsten?“, die genannte Person sagt, ob die Antwort stimmt).
- „Andere Frage“ tauscht eine Frage aus, ohne dass es etwas kostet.
- Spielform „Gemeinsam“: Alle sammeln zusammen Sterne, jede richtige Antwort bringt einen Stern für die ganze Familie. Es gibt keinen Verlierer. „Reihum“: Jede Person (oder jedes Team, optional „Teams bilden“) sammelt Punkte, am Ende gibt es eine Rangliste, auch mit Gleichstand.
- Vorlesen: Die Sprachausgabe des iPhones liest Frage und Antworten auf Deutsch vor. Einstellbar: für Klein und Mittel automatisch, nur per Knopf „Vorlesen“ oder aus. Dafür muss am iPhone der Ton an sein; bleibt es stumm, bitte Lautstärke und Stummschalter prüfen.
- Pause: Oben rechts „Beenden“ → „Pause machen“. Der Stand bleibt gespeichert, auf der Startseite steht „Familienrunde läuft“ mit „Fortsetzen“ und „Verwerfen“. Gespeichert werden Spielerinnen und Spieler, Punkte und die aktuelle Frage.
- Bereits gestellte Familienfragen werden vermerkt, damit sich Fragen nicht so schnell wiederholen. Die Sicherung enthält die Familienrunde-Einstellungen (Namen, Altersstufen, Spielform) und diese Liste.

## Eigene Wissensfragen

Über „Importieren“ auf dem Startbildschirm lassen sich weitere Fragen als JSON-Datei laden. Sie bleiben nur lokal im Browser des Handys gespeichert (nicht im öffentlichen Repo). Im Zwei-Handy-Modus zählen die Fragen von Handy 1. Format wie in `fragen.json`. Eine Sicherung (siehe unten) lässt sich auf demselben Weg wieder einspielen.

## Sicherung und Wiederherstellung

Startbildschirm → „Sicherung“. Eine Sicherung enthält eigene Wissensfragen, eigene Paarfragen, die Bilanz, Namen, die Einstellungen der Familienrunde (Namen und Altersstufen) und welche Fragen schon gestellt wurden.

- „Sicherung speichern / teilen“ öffnet auf dem iPhone das Teilen-Menü (z. B. „In Dateien sichern“ oder an sich selbst schicken). Ohne Teilen-Menü wird eine Datei heruntergeladen.
- „Als Text kopieren“ legt die Sicherung in die Zwischenablage, z. B. zum Einfügen in eine Notiz.
- „Wiederherstellen“ per Datei oder eingefügtem Text ergänzt Fehlendes. Vorhandene Fragen und Namen bleiben unverändert, die Bilanz wird übernommen, wenn sie mehr Spiele enthält.
- Auf dem Startbildschirm steht, wann zuletzt gesichert wurde. Nach 30 Tagen kommt ein Hinweis.
- Der „Verbindungstest“ hat oben und unten einen Link zurück zur App.

## Hinweis zum Speicher

Safari und die Home-Bildschirm-App haben getrennten Speicher. Am besten immer nur über das Home-Bildschirm-Symbol spielen und gelegentlich eine Sicherung erstellen (Startbildschirm → „Sicherung“).

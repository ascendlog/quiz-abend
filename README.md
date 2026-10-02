# Quiz-Abend

Quizspiel für zwei – gedacht für einen Spieleabend zu zweit, läuft als Web-App auf dem iPhone (Home-Bildschirm).

## Dateien

- `index.html` – die App: Wissensspiel „Wer weiß mehr?“ (ein Handy abwechselnd oder zwei Handys live) und der „Paarabend“ (zwei Handys)
- `fragen.json` – Fragenpaket (102 Fragen: Geografie, Geschichte, Natur & Wissenschaft inkl. Psychologie, Kultur, Sport, Mode)
- `paarfragen.json` – Vorschläge für den Paarabend (64 Fragen in drei Stufen, Freitext oder Auswahl)
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
- Bricht eine Verbindung ab (z. B. Sperrbildschirm), pausiert die Frage und läuft nach dem automatischen Wiederverbinden weiter.
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

## Eigene Wissensfragen

Über „Importieren“ auf dem Startbildschirm lassen sich weitere Fragen als JSON-Datei laden. Sie bleiben nur lokal im Browser des Handys gespeichert (nicht im öffentlichen Repo). Im Zwei-Handy-Modus zählen die Fragen von Handy 1. Format wie in `fragen.json`. Eine Sicherung (siehe unten) lässt sich auf demselben Weg wieder einspielen.

## Sicherung und Wiederherstellung

Startbildschirm → „Sicherung“. Eine Sicherung enthält eigene Wissensfragen, eigene Paarfragen, die Bilanz, Namen und welche Fragen schon gestellt wurden.

- „Sicherung speichern / teilen“ öffnet auf dem iPhone das Teilen-Menü (z. B. „In Dateien sichern“ oder an sich selbst schicken). Ohne Teilen-Menü wird eine Datei heruntergeladen.
- „Als Text kopieren“ legt die Sicherung in die Zwischenablage, z. B. zum Einfügen in eine Notiz.
- „Wiederherstellen“ per Datei oder eingefügtem Text ergänzt Fehlendes. Vorhandene Fragen und Namen bleiben unverändert, die Bilanz wird übernommen, wenn sie mehr Spiele enthält.
- Auf dem Startbildschirm steht, wann zuletzt gesichert wurde. Nach 30 Tagen kommt ein Hinweis.
- Der „Verbindungstest“ hat oben und unten einen Link zurück zur App.

## Hinweis zum Speicher

Safari und die Home-Bildschirm-App haben getrennten Speicher. Am besten immer nur über das Home-Bildschirm-Symbol spielen und gelegentlich eine Sicherung erstellen (Startbildschirm → „Sicherung“).

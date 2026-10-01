# Quiz-Abend

Quizspiel für zwei – gedacht für einen Spieleabend zu zweit, läuft als Web-App auf dem iPhone (Home-Bildschirm).

## Dateien

- `index.html` – das Spiel (Wissensspiel auf einem Handy, abwechselnd)
- `fragen.json` – Fragenpaket (102 Fragen: Geografie, Geschichte, Natur & Wissenschaft inkl. Psychologie, Kultur, Sport, Mode)
- `verbindungstest.html` – Test, ob sich zwei iPhones im WLAN direkt verbinden (Vorbereitung für den Modus „zwei Handys“)
- `icon.png` – Symbol für den Home-Bildschirm

## Spielregeln

- Fragetypen: Multiple Choice, Wahr/Falsch, Schätzfragen
- 10 Punkte pro richtige Antwort, bis zu 5 Zeitbonus-Punkte (20 s bei Auswahlfragen)
- Schätzfragen: Wer näher dran liegt, bekommt 10 Punkte, ein exakter Treffer gibt +5 (30 s)
- Joker pro Person: 1× 50:50, 1× Frage tauschen
- Spielende wählbar: feste Anzahl Fragen oder Zielpunkte

## Eigene Fragen

Über „Importieren“ auf dem Startbildschirm lassen sich weitere Fragen als JSON-Datei laden. Sie bleiben nur lokal im Browser des Handys gespeichert (nicht im öffentlichen Repo). Format wie in `fragen.json`. „Sichern“ exportiert importierte Fragen und die Bilanz.

## Hinweis zum Speicher

Safari und die Home-Bildschirm-App haben getrennten Speicher. Am besten immer nur über das Home-Bildschirm-Symbol spielen und gelegentlich „Sichern“ nutzen.

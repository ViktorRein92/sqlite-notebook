# 📝 sqlite-notebook
Ein einfaches, lokales Notizbuch mit Python und SQLite – zum Lernen von Git, GitHub und professionellen Projektstrukturen.

## 📚 Projektziel
Dieses Projekt dient dazu, die Grundlagen der Softwareentwicklung mit folgenden Schwerpunkten zu üben:

- 🧠 Arbeiten mit Git und GitHub (Branches, Commits, Push)
- 🛠️ Strukturierung von Python-Projekten
- 💻 Umgang mit virtuellen Umgebungen (`venv`)
- 📄 Dokumentation (`README.md`, `.gitignore`)
- 🐍 Erweiterbar mit Tests, Copilot und automatisierter Analyse

## 🏗️ Projektstruktur
```
sqlite-notebook/
├── main.py          # Hauptskript (Startpunkt)
├── sql.py           # SQLite-Datenbankfunktionen
├── tests/           # Testverzeichnis
│   └── test_sql.py  # Tests für die Datenbankfunktionen
├── docs/            # Dokumentation
│   └── development-setup.md  # Entwicklungsumgebung
├── notebook.db      # SQLite-Datenbank (wird erstellt)
├── test_report.html # HTML-Testreport
├── .gitignore       # Ignoriert virtuelle Umgebung, Cache & DB
├── README.md        # Diese Projektbeschreibung
└── .venv/           # Lokale virtuelle Umgebung (nicht im Repo)
```

## 🚀 Ausführen
```bash
python main.py
```

## 🔧 Funktionen (Stand: v0.2)
- ✅ Datenbankverbindung herstellen (`get_connection`)
- ✅ Notiztabelle erstellen (`create_table`)
- ✅ Notiz speichern (`save_note`)
- ✅ Alle Notizen abrufen (`get_notes`)
- ✅ Notiz nach Inhalt löschen (`delete_note`)
- ✅ Notiz nach ID löschen (`delete_note_by_id`)
- 🆕 CLI-Menü (in Entwicklung)

## 📈 Nächste Schritte
- [x] SQL-Datenbank integrieren  
- [x] Tests mit `pytest` hinzufügen
- [ ] CLI oder Menüsystem erstellen  
- [ ] Fehlerbehandlung verbessern
- [ ] Notizen nach Datum/Zeit sortieren
- [ ] Notizen bearbeiten

## 🧪 Tests ausführen
```bash
# HTML-Report erstellen
pytest --html=test_report.html --self-contained-html -v

# Oder mit Alias (falls in der Shell konfiguriert)
pytest-html
```

Die Tests überprüfen alle Datenbankfunktionen mit Test-Driven Development (TDD).

## 👨‍🔧 Entwickler

**Viktor Rein**  
Maschinenbaustudent mit Fokus auf KI & Software-Entwicklung  
GitHub: [@ViktorRein92](https://github.com/ViktorRein92)

---

> Dieses Projekt ist Teil meines Lernprozesses. Verbesserungsvorschläge, Pull Requests und Feedback sind willkommen! 🙌

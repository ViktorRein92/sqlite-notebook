import sys                  # Importiere das sys-Modul (für Zugriff auf Systempfade)
import os                   # Importiere das os-Modul (für Dateizugriffe und Pfadoperationen)
# Füge den übergeordneten Ordner zum Suchpfad hinzu, damit Python das sql-Modul finden kann
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sql                  # Importiere unser eigenes sql-Modul aus dem Hauptverzeichnis

# Hier kommen die neuen Tests rein

def test_get_connection():
    """
    Testet ob eine gültige Datenbankverbindung erstellt werden kann.
    
    Erwartet:
    - Verbindung ist nicht None
    - Verbindung kann geschlossen werden ohne Fehler
    """
    # Arrange (Vorbereitung) - hier nichts nötig
    
    # Arrange: Test-Datenbank anlegen
    conn = sql.get_connection("test_notebook.db")    # Erstelle eine Verbindung zu einer Test-Datenbank
    
    # Assert (Prüfung)
    assert conn is not None                          # Prüfe, ob die Verbindung existiert (nicht None ist)
    assert hasattr(conn, 'close')                    # Prüfe, ob die Verbindung eine close()-Methode hat
    
    # Cleanup (Aufräumen)
    conn.close()                                     # Schließe die Verbindung sauber

def test_create_table():
    """
    Testet, ob die Notiz-Tabelle korrekt erstellt wird.
    Erwartet:
    - Tabelle 'notes' wird erstellt
    """
    # Arrange: Test-Datenbank anlegen
    conn = sql.get_connection("test_notebook.db")        # Erstelle eine Verbindung zu einer Test-Datenbank
    
    # Act: Funktion aufrufen (existiert noch nicht!)
    sql.create_table(conn)                               # Rufe die zu testende Funktion auf
    
    # Assert: Prüfen, ob Tabelle existiert
    cursor = conn.cursor()                               # Erstelle einen Cursor zum Ausführen von SQL-Befehlen
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='notes'")  # Frage nach der Tabelle 'notes'
    assert cursor.fetchone() is not None                 # Prüfe, ob die Tabelle gefunden wurde
    
    # Cleanup: Verbindung schließen und Test-DB löschen
    conn.close()                                         # Schließe die Verbindung sauber
    os.remove("test_notebook.db")                        # Lösche die Testdatenbank

def test_save_note():
    """
    Testet, ob eine Notiz korrekt gespeichert wird.
    Erwartet:
    - Notiz wird in der Datenbank gespeichert
    """
    # Arrange: Test-Datenbank anlegen und Tabelle erstellen
    conn = sql.get_connection("test_notebook.db")        # Erstelle eine Verbindung zu einer Test-Datenbank
    sql.create_table(conn)                               # Stelle sicher, dass die Tabelle existiert
    
    # Act: Notiz speichern
    note = "Test-Notiz"                                  # Definiere den Inhalt der Test-Notiz
    sql.save_note(conn, note)                            # Rufe die zu testende Funktion auf
    
   # Assert: Prüfen, ob Notiz gespeichert wurde
    cursor = conn.cursor()                               # Erstelle einen Cursor zum Ausführen von SQL-Befehlen
    cursor.execute("SELECT content FROM notes WHERE content=?", (note,))  # Suche nach  der gespeicherten Notiz
    assert cursor.fetchone() is not None                 # Prüfe, ob die Notiz gefunden wurde
    
    # Cleanup: Verbindung schließen und Test-DB löschen
    conn.close()                                         # Schließe die Verbindung sauber
    os.remove("test_notebook.db")                        # Lösche die Testdatenbank

def test_get_notes():
    """
    Testet, ob alle gespeicherten Notizen korrekt abgerufen werden.
    Erwartet:
    - Liste der Notizen wird zurückgegeben
    """ 
    # Arrange: Test-Datenbank anlegen und Tabelle erstellen
    conn = sql.get_connection("test_notebook.db")        # Erstelle eine Verbindung zu einer Test-Datenbank
    sql.create_table(conn)                               # Stelle sicher, dass die Tabelle existiert
    
    # Act: Notizen speichern
    notes = ["Notiz 1", "Notiz 2", "Notiz 3"]           # Definiere mehrere Test-Notizen
    for note in notes:
        sql.save_note(conn, note)                        # Speichere jede Notiz
    
    # Assert: Prüfen, ob alle Notizen abgerufen werden können
    retrieved_notes = sql.get_notes(conn)                # Rufe die zu testende Funktion auf
    assert len(retrieved_notes) == len(notes)            # Prüfe, ob die Anzahl der abgerufenen Notizen stimmt
    for note in notes:
        assert note in retrieved_notes                    # Prüfe, ob jede Notiz in den abgerufenen Notizen enthalten ist
    
    # Cleanup: Verbindung schließen und Test-DB löschen
    conn.close()                                         # Schließe die Verbindung sauber
    os.remove("test_notebook.db")                        # Lösche die Testdatenbank


def test_delete_note():
    """
    Testet, ob eine Notiz korrekt gelöscht wird.
    Erwartet:
    - Notiz wird aus der Datenbank entfernt
    """
    # Arrange: Test-Datenbank anlegen und Tabelle erstellen
    conn = sql.get_connection("test_notebook.db")        # Erstelle eine Verbindung zu einer Test-Datenbank
    sql.create_table(conn)                               # Stelle sicher, dass die Tabelle existiert
    
    # Act: Notiz speichern
    note = "Zu löschende Notiz"                          # Definiere den Inhalt der zu löschenden Notiz
    sql.save_note(conn, note)                            # Speichere die Notiz
    
    # Act: Notiz löschen
    sql.delete_note(conn, note)                          # Rufe die zu testende Funktion auf
    
    # Assert: Prüfen, ob Notiz gelöscht wurde
    cursor = conn.cursor()                               # Erstelle einen Cursor zum Ausführen von SQL-Befehlen
    cursor.execute("SELECT content FROM notes WHERE content=?", (note,))  # Suche nach der gelöschten Notiz
    assert cursor.fetchone() is None                      # Prüfe, ob die Notiz nicht mehr gefunden wurde
    
    # Cleanup: Verbindung schließen und Test-DB löschen
    conn.close()                                         # Schließe die Verbindung sauber
    os.remove("test_notebook.db")                        # Lösche die Testdatenbank 

def test_delete_note_by_id():
    """
    Testet, ob eine Notiz anhand ihrer ID korrekt gelöscht wird.
    Erwartet:
    - Notiz wird aus der Datenbank entfernt
    """
    # Arrange: Test-Datenbank anlegen und Tabelle erstellen
    conn = sql.get_connection("test_notebook.db")        # Erstelle eine Verbindung zu einer Test-Datenbank
    sql.create_table(conn)                               # Stelle sicher, dass die Tabelle existiert

    # Act: Notiz speichern
    note = "Zu löschende Notiz"                          # Definiere den Inhalt der zu löschenden Notiz
    sql.save_note(conn, note)                            # Speichere die Notiz

    # Hole die ID der gespeicherten Notiz
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM notes WHERE content=?", (note,))
    row = cursor.fetchone()
    assert row is not None                               # Stelle sicher, dass die Notiz existiert
    note_id = row[0]

    # Act: Notiz anhand der ID löschen
    sql.delete_note_by_id(conn, note_id)                 # Rufe die zu testende Funktion auf

    # Assert: Prüfen, ob Notiz gelöscht wurde
    cursor.execute("SELECT content FROM notes WHERE id=?", (note_id,))
    assert cursor.fetchone() is None                     # Prüfe, ob die Notiz nicht mehr gefunden wurde

    # Cleanup: Verbindung schließen und Test-DB löschen
    conn.close()                                         # Schließe die Verbindung sauber
    os.remove("test_notebook.db")                        # Lösche die Testdatenbank
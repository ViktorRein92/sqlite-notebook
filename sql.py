"""
sql.py

Beschreibung:
Modul für die Datenbankfunktionen des sqlite-notebook-Projekts. 
Stellt Funktionen bereit, um eine Verbindung zu einer lokalen SQLite-Datenbank herzustellen, Notizen zu speichern, abzurufen und zu löschen. 
Alle SQL-Operationen werden gekapselt, sodass die Hauptlogik in main.py übersichtlich bleibt.

Funktionen:
- Verbindung zur SQLite-Datenbank aufbauen
- Notiz-Tabelle anlegen (falls nicht vorhanden)
- Neue Notiz speichern
- Notizen abrufen
- Notiz löschen
- Fehlerbehandlung für Datenbankoperationen

Voraussetzungen:
- Python 3.x
- Standardbibliothek: sqlite3

Autor: Viktor Rein
"""


from importlib.resources import contents
import sqlite3

def get_connection(db_name="notebook.db"):
    """
    Stellt eine Verbindung zur SQLite-Datenbank her.
    Legt die Datei an, falls sie noch nicht existiert.
    
    Args:
        db_name: Name der Datenbankdatei
        
    Returns:
        sqlite3.Connection: Datenbankverbindung
    """
    return sqlite3.connect(db_name)



# In sql.py hinzufügen:
def create_table(conn):
    """
    Erstellt die Notiz-Tabelle, falls sie noch nicht existiert.
    
    Args:
        conn: SQLite-Datenbankverbindung
    """
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY,
        content TEXT
    )
    """)
    conn.commit()

def save_note(conn, note_text):
    """
    Speichert eine neue Notiz in der Datenbank.
    
    Args:
        conn: SQLite-Datenbankverbindung
        note_text: Inhalt der Notiz
    """
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notes (content) VALUES (?)", (note_text,))
    conn.commit()

def get_notes(conn):
    """
    Ruft alle Notizen aus der Datenbank ab.
    
    Args:
        conn: SQLite-Datenbankverbindung
        
    Returns:
        list: Liste der Notizen als Tupel (id, content)
    """
    cursor = conn.cursor()
    cursor.execute("SELECT id, content FROM notes")
    rows = cursor.fetchall()
    return [row[1] for row in rows]

def delete_note(conn, note):
    """
    Löscht eine Notiz aus der Datenbank.
    """
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE content=?", (note,))
    conn.commit()

def delete_note_by_id(conn, note_id):
    """
    Löscht eine Notiz aus der Datenbank anhand ihrer ID.
    """
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE id=?", (note_id,))
    conn.commit()
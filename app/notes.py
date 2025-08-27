import json
import uuid
from datetime import datetime

NOTES_FILE = "data/notes.json"

def load_notes():
    with open(NOTES_FILE, "r") as f:
        return json.load(f)

def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=2)

def add_note(title, body):
    notes = load_notes()
    note = {
        "id": str(uuid.uuid4()),
        "title": title,
        "body": body,
        "created_at": datetime.now().isoformat()
    }
    notes.append(note)
    save_notes(notes)
    return note

def list_notes():
    """Devuelve todas las notas"""
    return load_notes()

def find_notes(query):
    """Devuelve notas cuyo título o cuerpo contenga la query"""
    notes = load_notes()
    return [n for n in notes if query.lower() in n['title'].lower() or query.lower() in n['body'].lower()]

def delete_note(note_id):
    """Elimina una nota por su ID. Devuelve True si se eliminó, False si no existe."""
    notes = load_notes()
    new_notes = [n for n in notes if n["id"] != note_id]

    if len(new_notes) == len(notes):
        return False  # no se eliminó nada

    save_notes(new_notes)
    return True
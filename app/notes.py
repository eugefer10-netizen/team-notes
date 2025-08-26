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

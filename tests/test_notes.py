import os
import json
import pytest
from app import notes

# Usar un archivo temporal de notas para no romper el real
TEST_FILE = "data/test_notes.json"

@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Antes de cada test, crear un archivo vacío
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    with open(TEST_FILE, "w") as f:
        json.dump([], f)

    # Cambiar archivo de notas por el de prueba
    original_file = notes.NOTES_FILE
    notes.NOTES_FILE = TEST_FILE

    yield  # 👉 aquí se ejecuta el test

    # Después de cada test, restaurar archivo original
    notes.NOTES_FILE = original_file
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

def test_add_note():
    note = notes.add_note("Titulo", "Cuerpo")
    assert note["title"] == "Titulo"
    assert note["body"] == "Cuerpo"
    assert len(notes.list_notes()) == 1

def test_find_notes():
    notes.add_note("Buscarme", "contenido")
    results = notes.find_notes("buscarme")
    assert len(results) == 1
    assert results[0]["title"] == "Buscarme"

def test_delete_note():
    note = notes.add_note("Borrar", "nota")
    deleted = notes.delete_note(note["id"])
    assert deleted is True
    assert len(notes.list_notes()) == 0

import os
import json
from .embeddings import embed_text

NOTES_FOLDER = "notes" # folder where notes are stored
INDEX_FILE = "helix_index.json" # index file to store embeddings

def load_all_notes() -> dict: # defines function to load all notes
    """
    Returns {filename: text} for every .txt file in the notes folder.
    """
    notes = {} #dictionary to store notes

    for file in os.listdir(NOTES_FOLDER): # iterates through each file in notes folder
        if file.endswith(".txt"): # checks if file is a .txt file
            path = os.path.join(NOTES_FOLDER, file) # creates full file path
            with open(path, "r", encoding="utf-8") as f: # opens file in read mode with utf-8 encoding
                notes[file] = f.read() # stores file content in dictionary

    return notes # returns dictionary of notes

def build_index() -> list: # defines function to build index
    """
    Reads all notes, embeds them, returns a list of entries:
    [
        {"file": "...", "text": "...", "vector": [...]},
        ...
    ]
    """
    notes = load_all_notes() # loads all notes
    index = [] # list to store index entries

    for filename, text in notes.items(): # iterates through each note
        vector = embed_text(text) # embeds the note text
        index.append({  # creates index entry
            "file": filename,
            "text": text,
            "vector": vector
        })
    return index # returns the index list

def rebuild_index():
    """
    Rebuild Helix vector index from all notes.
    """
    index = build_index()
    save_index(index)
    return index

def save_index(index: list): # defines function to save index
    with open(INDEX_FILE, "w", encoding="utf-8") as f: # opens index file in write mode with utf-8 encoding
        json.dump(index, f, indent=2) # saves index as JSON

def load_index() -> list: # defines function to load index
    if not os.path.isfile(INDEX_FILE): # checks if index file exists
        return [] # returns empty list if file does not exist

    with open(INDEX_FILE, "r", encoding="utf-8") as f: # opens index file in read mode with utf-8 encoding
        return json.load(f) # loads index from JSON




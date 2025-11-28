import os #os allows work with files & folders
from datetime import datetime #datetime timestamps notes

NOTES_DIR = "notes" #directory for notes

if not os.path.exists(NOTES_DIR): #makes sure notes directory exists
    os.makedirs(NOTES_DIR)

def add_note(): #defines function to add a note
    """
    Create a new note and save it in the notes/ directory. # Documentation string for add_note function
    """
    title = input("Enter note title: ").strip() #stores its title into var called title from user and strips whitespace
    if not title:
        print("Title cannot be empty.") #checks if title is empty
        return

    content = input("Write your note:\n") #creates var content to store note content from user input

    filename = os.path.join(NOTES_DIR, f"{title}.txt") #creates filename var to store full file path
    with open(filename, "w", encoding="utf-8") as f: #opens file in write mode with utf-8 encoding
        f.write(f"Created: {datetime.now()}\n\n") #writes timestamp to file
        f.write(content) #writes note content to file

    print(f"note '{title}' saved.") #confirms note created

def list_notes(): #defines function to list notes
    """
    Show all notes stored in the notes/ directory.
    """
    files = os.listdir(NOTES_DIR) #lists all files in notes directory
    txt_files = [f.replace(".txt","") for f in files if f.endswitch(".txt")] #filters only .txt files and removes extension for display
    if not txt_files: #checks if there are no notes
        print("No notes found.")
        return
    print("\nYour Notes:") #prints header
    for title in sorted(txt_files): #sorts titles alphabetically
        print("- " + title) #prints each note title with a dash

def view_note(): #defines function to view a note
    """
    Load a single note and print its content
    """
    title = input("Enter note name to view: ").strip() #gets note title from user input & strips whitespace
    filename = os.path.join(NOTES_DIR, f"{title}.txt") #creates full file path

    if not os.path.isfile(filename): #checks if file exists
        print("Note not found.")
        return

    with open(filename, "r", encoding="utf-8") as f: #opens file in read mode with utf-8 encoding
        print(*"\n=== Note Content ===") #prints header
        print(f.read()) #prints file content
def search_notes():
    """
    Search for notes containing a specific keyword.
    """
    keyword = input("Enter keyword: ").strip().lower()   #gets keyword from user input & strips whitespace
    if not keyword:
        print("Keyword cannot be empty.") #checks if keyword is empty
        return

    found_any = False #flag to track if any notes were found

    for file in os.listdir(NOTES_DIR): #iterates through each file
        if file.endswith(".txt"): #checks if file is a .txt file
            filepath = os.path.join(NOTES_DIR, file) #creates full file path
            with open(filepath, "r", encoding="utf-8") as f: #opens file in read mode with utf-8 encoding
                text = f.read().lower()

                if keyword in text:
                    print(f"- Found in: {file.replace('.txt','')}") #prints note title where keyword was found
                    found_any = True

    if not found_any:
        print("No matches found.")

def delete_note():
    """
    Delete a note from the notes/ folder.
    """
    title = input("Enter note name to delete: ").strip() #gets note title from user input & strips whitespace
    filename = os.path.join(NOTES_DIR, f"{title}.txt") #creates full file path

    if os.path.isfile(filename): #checks if file exists
        os.remove(filename)
        print(f"Deleted note '{title}'.") #confirms deletion
    else:
        print("Note not found.")



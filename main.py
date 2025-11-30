from nexus_brain.knowledge import add_note, list_notes, view_note, search_notes, delete_note
from helix.ask import answer_question
from helix.indexer import rebuild_index

def show_menu():
    print("\n=== Nexus Knowledge Base ===")
    print("1. Add Note")
    print("2. List Notes")
    print("3. View Note")
    print("4. Search Notes (Keyword)")
    print("5. Delete Note")
    print("6. Ask Helix (AI Search)")
    print("7. Exit")


def initialize_helix():
    print("[INFO] Building Helix Vector Index...")
    rebuild_index()
    print("[INFO] Helix is ready!\n")


def main():
    initialize_helix()   # Build vector index *before* showing menu

    while True:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            add_note()

        elif choice == "2":
            list_notes()

        elif choice == "3":
            view_note()

        elif choice == "4":
            search_notes()   # keyword search

        elif choice == "5":
            delete_note()

        elif choice == "6":
            query = input("\nAsk Nexus something: ")
            answer = answer_question(query)
            print("\n--- Helix Answer ---")
            print(answer)
            print("---------------------\n")

        elif choice == "7":
            print("Exiting Nexus. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()

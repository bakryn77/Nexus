from knowledge import add_note, list_notes, view_note, search_notes, delete_note

def show_menu():
    print("\nKnowledge Base Menu:")
    print("1. Add Note")
    print("2. List Notes")
    print("3. View Note")
    print("4. Search Notes")
    print("5. Delete Note")
    print("6. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_note()
        elif choice == "2":
            list_notes()
        elif choice == "3":
            view_note()
        elif choice == "4":
            search_notes()
        elif choice == "5":
            delete_note()
        elif choice == "6":
            print("Exiting Knowledge Base. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
if __name__ == "__main__":
    main()
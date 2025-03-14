import sys
import os

# Add the project root directory to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(project_root)


from lib.crud.book_crud import create_book, get_all_books, find_book_by_id, update_book, delete_book
from lib.crud.member_crud import create_member, get_all_members, find_member_by_id, update_member, delete_member
from lib.crud.librarian_crud import get_all_librarians, create_librarian, delete_librarian, get_librarian_by_id, update_librarian
from lib.crud.borrow_record_crud import create_borrow_record, update_borrow_record, get_all_borrow_records
from lib.crud.author_crud import get_all_authors, create_author, find_author_by_id, update_author, delete_author

# Helper: Verify librarian credentials
def verify_librarian():
    response = input("Are you a librarian? (y/n): ").strip().lower()
    if response == 'y':
        lib_id = input("Enter your Librarian ID: ").strip()
        lib_name = input("Enter your Name: ").strip()
        librarian = get_librarian_by_id(int(lib_id))
        if librarian and librarian.name and librarian.name.lower() == lib_name.lower():
            return True, librarian
        else:
            print("Verification failed.")
            return False, None
    else:
        print("Please ask a librarian to perform this action.")
        return False, None

# Helper: Post action prompt using number-based input
def post_action_prompt():
    print("\nEnter 1 to Exit or 2 to return to the Main Menu:")
    choice = input().strip()
    if choice == '1':
        return "exit"
    elif choice == '2':
        return "main"
    else:
        print("Invalid input. Returning to Main Menu.")
        return "main"

# Main Menu
def main_menu():
    while True:
        print("\n====== Library Management System ======")
        print("1. Borrow a Book")
        print("2. Return a Book")
        print("3. List All Books")
        print("4. Manage Books (Librarian Only)")
        print("5. Manage Members (Librarian Only)")
        print("6. Manage Librarians")
        print("7. Exit")
        choice = input("Select an option (1-7): ").strip()

        if choice == "1":
            borrow_book_menu()
        elif choice == "2":
            return_book_menu()
        elif choice == "3":
            list_books_menu()
        elif choice == "4":
            manage_books_menu()
        elif choice == "5":
            manage_members_menu()
        elif choice == "6":
            manage_librarians_menu()
        elif choice == "7":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Borrow a Book (Member action)
def borrow_book_menu():
    print("\n--- Borrow a Book ---")
    member_id = input("Enter your Member ID: ").strip()
    book_id = input("Enter the Book ID to borrow: ").strip()
    
    # Require librarian verification for issuing a book
    print("A librarian must verify to issue a book.")
    verified, librarian = verify_librarian()
    if not verified:
        print("Librarian verification failed. Cannot borrow the book.")
        return

    # Now, pass the verified librarian's ID instead of None
    result = create_borrow_record(int(book_id), int(member_id), librarian.id)
    if result:
        print("Book borrowed successfully!")
    if post_action_prompt() == "exit":
        exit(0)


# Return a Book (Member action)
def return_book_menu():
    print("\n--- Return a Book ---")
    record_id = input("Enter the Borrow Record ID: ").strip()
    # Update the borrow record with a return date and increase available copies.
    from datetime import datetime, timezone
    update_borrow_record(int(record_id), return_date=datetime.now(timezone.utc))

    print("Book returned successfully!")
    if post_action_prompt() == "exit":
        exit(0)

# List All Books (Accessible to everyone)
def list_books_menu():
    print("\n--- List of All Books ---")
    books = get_all_books()
    if not books:
        print("No books found.")
    else:
        for book in books:
            print(f"ID: {book.id} | Title: {book.title} | Genre: {book.genre} | Copies Available: {book.copies_available}")
    if post_action_prompt() == "exit":
        exit(0)

# Manage Books (Librarian Only)
def manage_books_menu():
    verified, librarian = verify_librarian()
    if not verified:
        if post_action_prompt() == "exit":
            exit(0)
        return

    while True:
        print("\n--- Manage Books (Librarian Only) ---")
        print("1. Add Book")
        print("2. Delete Book")
        print("3. Back to Main Menu")
        choice = input("Select an option (1-3): ").strip()
        
        if choice == "1":
            print("\n--- Add Book ---")
            title = input("Enter Book Title: ").strip()
            author_name = input("Enter Author Name: ").strip()
            # Lookup author by name; if not found, create a new author.
            from lib.crud.author_crud import find_author_by_name, create_author
            author = find_author_by_name(author_name)
            if not author:
                print("Author not found. Creating new author.")
                author_id_value = create_author(author_name)  # Now returns the new author's ID (an integer)
            else:
                author_id_value = author.id
            genre = input("Enter Genre: ").strip()
            copies_available = input("Enter Number of Copies: ").strip()
            create_book(title, author_id_value, genre, int(copies_available), librarian.id)
            print("Book added successfully!")
        elif choice == "2":
            print("\n--- Delete Book ---")
            book_id = input("Enter Book ID to delete: ").strip()
            delete_book(int(book_id))
            print("Book deleted successfully!")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
    if post_action_prompt() == "exit":
        exit(0)

# Manage Members (Librarian Only)
def manage_members_menu():
    verified, _ = verify_librarian()
    if not verified:
        if post_action_prompt() == "exit":
            exit(0)
        return

    while True:
        print("\n--- Manage Members (Librarian Only) ---")
        print("1. List All Members")
        print("2. Add Member")
        print("3. Delete Member")
        print("4. Back to Main Menu")
        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            members = get_all_members()
            if not members:
                print("No members found.")
            else:
                for member in members:
                    print(f"ID: {member.id} | Name: {member.name} | Email: {member.email}")
        elif choice == "2":
            print("\n--- Add Member ---")
            name = input("Enter Member Name: ").strip()
            email = input("Enter Member Email: ").strip()
            create_member(name, email)
            print("Member added successfully!")
        elif choice == "3":
            print("\n--- Delete Member ---")
            member_id = input("Enter Member ID to delete: ").strip()
            delete_member(int(member_id))
            print("Member deleted successfully!")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
    if post_action_prompt() == "exit":
        exit(0)

# Manage Librarians (Admin-level actions)
def manage_librarians_menu():
    while True:
        print("\n--- Manage Librarians ---")
        print("1. List All Librarians")
        print("2. Add Librarian")
        print("3. Delete Librarian")
        print("4. Back to Main Menu")
        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            librarians = get_all_librarians()
            if not librarians:
                print("No librarians found.")
            else:
                for lib in librarians:
                    print(f"ID: {lib.id} | Name: {lib.name} | Employee ID: {lib.employee_id} | Email: {lib.email}")
        elif choice == "2":
            print("\n--- Add Librarian ---")
            name = input("Enter Librarian Name: ").strip()
            employee_id = input("Enter Employee ID: ").strip()
            email = input("Enter Email: ").strip()
            create_librarian(name, employee_id, email)
            print("Librarian added successfully!")
        elif choice == "3":
            print("\n--- Delete Librarian ---")
            lib_id = input("Enter Librarian ID to delete: ").strip()
            delete_librarian(int(lib_id))
            print("Librarian deleted successfully!")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
    if post_action_prompt() == "exit":
        exit(0)

if __name__ == "__main__":
    main_menu()

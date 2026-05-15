# q2_library_system.py

# Function to add a book
def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)
    print(f"Book '{title}' added successfully.")


# Function to borrow a book
def borrow_book(catalog, borrowed_books, book_id):
    if book_id in catalog:
        if book_id not in borrowed_books:
            borrowed_books.append(book_id)
            print(f"Book ID {book_id} borrowed successfully.")
        else:
            print(f"Book ID {book_id} is already borrowed.")
    else:
        print(f"Book ID {book_id} does not exist.")


# Function to return a book
def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Book ID {book_id} returned successfully.")
    else:
        print(f"Book ID {book_id} was not borrowed.")


# Function to register a member
def register_member(members, member_id):
    members.add(member_id)   # Set automatically ignores duplicates


# Function to show available books
def show_available(catalog, borrowed_books):
    print("\nAvailable Books:")

    for book_id, details in catalog.items():
        if book_id not in borrowed_books:
            title, author, year = details
            print(f"ID: {book_id}, Title: {title}, Author: {author}, Year: {year}")


# Main function
def main():

    # Dictionary for catalog
    catalog = {}

    # List for borrowed books
    borrowed_books = []

    # Set for members
    members = set()

    # Adding 4 books
    add_book(catalog, 101, "Python Basics", "John Smith", 2020)
    add_book(catalog, 102, "Data Structures", "Alice Brown", 2019)
    add_book(catalog, 103, "Machine Learning", "David Lee", 2021)
    add_book(catalog, 104, "Database Systems", "James Miller", 2018)

    # Registering members
    register_member(members, 1)
    register_member(members, 2)
    register_member(members, 3)
    register_member(members, 2)   # Duplicate member

    print("\nRegistered Members:", members)

    # Borrowing books
    borrow_book(catalog, borrowed_books, 101)
    borrow_book(catalog, borrowed_books, 103)

    # Returning one book
    return_book(borrowed_books, 101)

    # Display available books
    show_available(catalog, borrowed_books)


# Run program
main()
class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Copies Available: {self.copies}"


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author, copies):
        if title in self.books:
            self.books[title].copies += copies
        else:
            self.books[title] = Book(title, author, copies)
        print(f"Added {copies} copies of '{title}' by {author} to the library.")

    def remove_book(self, title, copies):
        if title in self.books:
            if self.books[title].copies > copies:
                self.books[title].copies -= copies
                print(f"Removed {copies} copies of '{title}' from the library.")
            elif self.books[title].copies == copies:
                del self.books[title]
                print(f"'{title}' has been completely removed from the library.")
            else:
                print(f"Not enough copies of '{title}' to remove.")
        else:
            print(f"'{title}' does not exist in the library.")

    def issue_book(self, title, user):
        if title in self.books and self.books[title].copies > 0:
            self.books[title].copies -= 1
            print(f"'{title}' has been issued to {user}.")
        else:
            print(f"'{title}' is not available.")

    def return_book(self, title, user):
        if title in self.books:
            self.books[title].copies += 1
            print(f"'{title}' has been returned by {user}.")
        else:
            print(f"'{title}' does not belong to this library. Adding it to the collection.")
            self.add_book(title, "Unknown", 1)

    def display_books(self):
        print("\nAvailable Books in the Library:")
        for book in self.books.values():
            print(book)


class LibraryManagementSystem:
    def __init__(self):
        self.library = Library()

    def menu(self):
        while True:
            print("\n=== Library Management System ===")
            print("1. Add Book")
            print("2. Remove Book")
            print("3. Issue Book")
            print("4. Return Book")
            print("5. Display Books")
            print("6. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                title = input("Enter book title: ")
                author = input("Enter author name: ")
                copies = int(input("Enter number of copies: "))
                self.library.add_book(title, author, copies)

            elif choice == "2":
                title = input("Enter book title: ")
                copies = int(input("Enter number of copies to remove: "))
                self.library.remove_book(title, copies)

            elif choice == "3":
                title = input("Enter book title: ")
                user = input("Enter your name: ")
                self.library.issue_book(title, user)

            elif choice == "4":
                title = input("Enter book title: ")
                user = input("Enter your name: ")
                self.library.return_book(title, user)

            elif choice == "5":
                self.library.display_books()

            elif choice == "6":
                print("Exiting the Library Management System. Goodbye!")
                break

            else:
                print("Invalid choice! Please try again.")


# Run the system
if __name__ == "__main__":
    system = LibraryManagementSystem()
    system.menu()

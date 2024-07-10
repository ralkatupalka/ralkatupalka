class Book:
    def __init__(self, title, author, isbn, year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.is_available = True

class User:
    def __init__(self, username, full_name):
        self.username = username
        self.full_name = full_name
        self.borrowed_books = []

class Library:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f'Book "{book.title}" added to the library.')

    def remove_book(self, isbn):
        book = next((b for b in self.books if b.isbn == isbn), None)
        if book:
            self.books.remove(book)
            print(f'Book "{book.title}" removed from the library.')
        else:
            print(f'No book found with ISBN {isbn}.')

    def search_book_by_title(self, title):
        found_books = [b for b in self.books if title.lower() in b.title.lower()]
        if found_books:
            for book in found_books:
                print(f'Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Year: {book.year}, Available: {book.is_available}')
        else:
            print(f'No book found with title containing "{title}".')

    def list_all_books(self):
        for book in self.books:
            print(f'Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Year: {book.year}, Available: {book.is_available}')

    def register_user(self, user):
        self.users.append(user)
        print(f'User "{user.username}" registered.')

    def borrow_book(self, isbn, username):
        user = next((u for u in self.users if u.username == username), None)
        book = next((b for b in self.books if b.isbn == isbn), None)
        if user and book and book.is_available:
            book.is_available = False
            user.borrowed_books.append(book)
            print(f'Book "{book.title}" borrowed by user "{username}".')
        elif not user:
            print(f'User "{username}" not found.')
        elif not book:
            print(f'Book with ISBN {isbn} not found.')
        elif not book.is_available:
            print(f'Book "{book.title}" is currently unavailable.')

    def return_book(self, isbn, username):
        user = next((u for u in self.users if u.username == username), None)
        if user:
            book = next((b for b in user.borrowed_books if b.isbn == isbn), None)
            if book:
                book.is_available = True
                user.borrowed_books.remove(book)
                print(f'Book "{book.title}" returned by user "{username}".')
            else:
                print(f'User "{username}" did not borrow a book with ISBN {isbn}.')
        else:
            print(f'User "{username}" not found.')

def main():
    library = Library("My Library", "123 Library St")

    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book by Title")
        print("4. List All Books")
        print("5. Register User")
        print("6. Borrow Book")
        print("7. Return Book")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            year = int(input("Enter year of publication: "))
            book = Book(title, author, isbn, year)
            library.add_book(book)

        elif choice == '2':
            isbn = input("Enter book ISBN to remove: ")
            library.remove_book(isbn)

        elif choice == '3':
            title = input("Enter book title to search: ")
            library.search_book_by_title(title)

        elif choice == '4':
            library.list_all_books()

        elif choice == '5':
            username = input("Enter username: ")
            full_name = input("Enter full name: ")
            user = User(username, full_name)
            library.register_user(user)

        elif choice == '6':
            username = input("Enter your username: ")
            isbn = input("Enter ISBN of the book to borrow: ")
            library.borrow_book(isbn, username)

        elif choice == '7':
            username = input("Enter your username: ")
            isbn = input("Enter ISBN of the book to return: ")
            library.return_book(isbn, username)

        elif choice == '8':
            print("Exiting the library system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
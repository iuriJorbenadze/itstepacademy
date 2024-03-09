from abc import ABC, abstractmethod
import json
import os

class IBookManager(ABC):
    @abstractmethod
    def add_book(self, title, author, publication_year):
        pass

    @abstractmethod
    def show_books(self):
        pass

    @abstractmethod
    def search_books_by_title(self, title):
        pass

    @abstractmethod
    def search_books_by_author(self, author):
        pass

    @abstractmethod
    def search_books_by_id(self, book_id):
        pass


class Book:
    def __init__(self, id, title, author, publication_year):
        self.id = id
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __str__(self):
        return f"[ID: {self.id}] '{self.title}' by {self.author}, published in {self.publication_year}"



class BookManager:
    def __init__(self, filename='books_database.json'):
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the file path by joining the script directory with the filename
        self.filepath = os.path.join(script_dir, filename)
        self.books = []  # List to store books

        self._init_database()
        self._load_books_from_file()
        self._current_id = max([book.id for book in self.books], default=0) + 1

    def _init_database(self):
        try:
            #Creates file, if exists throws FileExistsError
            open(self.filepath, 'x').close()
            self._save_books_to_file()  # Save initial empty list
        except FileExistsError:
            pass

    def _load_books_from_file(self):
        # Load books from the JSON file
        try:
            with open(self.filepath, 'r') as file:
                book_data = json.load(file)
                # print(book_data)
                self.books = [Book(**data) for data in book_data]
        except json.JSONDecodeError:
            self.books = []

    def _save_books_to_file(self):
        # Save the list of books to the JSON file
        with open(self.filepath, 'w') as file:
            json.dump([book.__dict__ for book in self.books], file)

    def add_book(self, title, author, publication_year):
        # Add a new book with auto-increment ID
        new_book = Book(self._current_id, title, author, publication_year)
        self.books.append(new_book)
        self._save_books_to_file()
        self._current_id += 1

    def show_books(self):
        # Display all books
        if not self.books:
            print("No books available.")
        for book in self.books:
            print(book)

    def search_books_by_title(self, title):
        # Search for books by title
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        self._print_search_results(found_books)

    def search_books_by_author(self, author):
        # Search for books by author
        found_books = [book for book in self.books if author.lower() in book.author.lower()]
        self._print_search_results(found_books)

    def search_books_by_id(self, book_id):
        # Search for books by ID
        found_books = [book for book in self.books if book.id == book_id]
        self._print_search_results(found_books)

    def _print_search_results(self, found_books):
        # Print search results
        if found_books:
            for book in found_books:
                print(book)
        else:
            print("No books found matching the criteria.")




def main(book_manager: IBookManager):
    while True:
        print("\nBook Manager")
        print("1. Add a Book")
        print("2. View All Books")
        print("3. Search Books by Title")
        print("4. Search Books by Author")
        print("5. Search Books by ID")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")

            # Not adding number checks on publication year, in case book year must be specified with B.C.E and so on.
            publication_year = input("Enter publication year: ")
            book_manager.add_book(title, author, publication_year)
            print("Book added successfully.")
        elif choice == '2':
            book_manager.show_books()
        elif choice == '3':
            title = input("Enter title to search for: ")
            book_manager.search_books_by_title(title)
        elif choice == '4':
            author = input("Enter author to search for: ")
            book_manager.search_books_by_author(author)
        elif choice == '5':
            book_id = int(input("Enter book ID to search for: "))
            book_manager.search_books_by_id(book_id)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    # Here you could instantiate any class that implements IBookManager
    book_manager_instance = BookManager()
    main(book_manager_instance)
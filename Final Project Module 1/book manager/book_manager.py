from abc import ABC, abstractmethod


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

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
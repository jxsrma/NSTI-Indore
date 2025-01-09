from abc import ABC, abstractmethod


class LibraryMember(ABC):
    @abstractmethod
    def borrow_book():
        pass

    def return_book():
        pass


class User(LibraryMember):
    name: str
    user_id: int

    def __init__(self, name, userId):
        self.name = name
        self.user_id = userId


class Librarian(User):
    def __init__(self, name, userId):
        Library.__init__(name, userId)

    def add_book(book_id):
        print("book added")

    def remove_book(book_id):
        print("book removed")


lib = Librarian("j", 124)
lib.add_book()


class Library:

    def __init__(self, books):
        self.__books = ["Python Programming",
                        "Data Structures", "Algorithms", "Machine Learning"]

    def display_books(self):
        for i in self.books:
            print(i)

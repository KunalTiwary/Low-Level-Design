class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

class BookList:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __str__(self):
        return ", ".join([str(book) for book in self.books])

# Aggregate
class Library:
    def __init__(self, booksList):
        self.booksList = booksList

    def createIterator(self):
        return BookIterator(self.booksList)


from abc import ABC, abstractmethod
class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass


class BookIterator(Iterator):
    def __init__(self, book_list):
        self.book_list = book_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.has_next():
            book = self.book_list.books[self.index]
            self.index += 1
            return book
        else:
            raise StopIteration

    def has_next(self):
        return self.index < len(self.book_list.books)


book_list = BookList()
book_list.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
book_list.add_book(Book("1984", "George Orwell"))
book_list.add_book(Book("Pride and Prejudice", "Jane Austen"))
iterator = Library(book_list).createIterator()

while iterator.has_next():
    book = next(iterator)
    print(book)
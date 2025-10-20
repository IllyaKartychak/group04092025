class Book:
    def __init__(self, author_name: str, book_name: str, book_id: int):
        if not book_name.strip():
            raise ValueError('Name not provided')
        self.author_name = author_name.title()
        self.book_name = book_name.title()
        self.id = book_id


class Library:
    def __init__(self, name: str):
        self.name = name
        self.book_list = []

    def add_book(self, new_book: Book):
        self.book_list.append(new_book)

    def remove_book(self, book_id: int):
        for book in self.book_list:
            if book.id == book_id:
                self.book_list.remove(book)
                return


book1 = Book(author_name="Alex", book_name="Harry Potter", book_id=1)
print(book1.id)
library = Library(name="OOP")
new_book1 = Book(author_name="Alex", book_name="Harry Potter", book_id=2)
library.add_book(new_book1)
print(library.book_list)
library.remove_book(new_book1.id)
print(library.book_list)

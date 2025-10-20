import pytest

from oop.hw_oop import Book, Library


# @pytest.fixture()
# @pytest.fixture(scope='function')
@pytest.fixture(scope='class')
# @pytest.fixture(scope='module')
# @pytest.fixture(scope='session')
def book1() -> Book:
    book = Book(book_name='ukrlit', author_name="Zabolotnij", book_id=1)
    yield book
    print(book, 'destroyed')


@pytest.fixture(scope='class')
def book2() -> Book:
    book = Book(book_name='Harry Potter', author_name="Roaling", book_id=2)
    return book


@pytest.fixture(scope='class')
def library1() -> Library:
    library = Library('Pet Library123')
    return library

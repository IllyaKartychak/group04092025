import pytest
from pytest import raises
from oop.hw_oop import Book


class TestBook:
    def test_new_book(self, book1):
        print(book1)
        assert book1.book_name
        assert book1.id
        assert book1.author_name

    def test_new_persons_diff_id(self, book1, book2):
        print(book2)
        assert book1.id != book2.id


class TestCreateNewBook:
    # def test_create_person_no_name(self):
    #     with raises(ValueError):
    #         Person("")
    #
    # def test_create_person_name_as_whitespaces(self):
    #     with raises(ValueError):
    #         Person("              ")

    @pytest.mark.parametrize("wrong_name", ["", "        ", '\n', '\t    '])
    def test_wrong_name(self, wrong_name: str):
        with raises(ValueError):
            Book(book_name=wrong_name, author_name="Alex", book_id=1)

    def test_new_book(self, book1):
        print(book1)
        assert book1.book_name
        assert book1.id
        assert book1.book_name == 'Ukrlit'

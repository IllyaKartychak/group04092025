class TestLibrary:
    def test_library(self, library1):
        assert library1.name
        assert not library1.book_list

    def test_library2(self, library1):
        assert library1.name
        assert not library1.book_list

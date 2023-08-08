from lib.book import Book 

"""
Call instance of book class
check fields are init
"""
def test_fields_correct():
    book = Book(1, 'Mockingbird', 'John')
    assert book.id == 1
    assert book.title == 'Mockingbird'
    assert book.author_name == 'John'

"""
Call instance of books
check __repr__ returns formated string of book info
"""
def test_for_formatted_string():
    book = Book(1, 'Mockingbird', 'John')
    assert str(book) == '1 - Mockingbird - John'


"""
check __eq__ is works
can compare different instances
"""
def test_books_are_equal():
    book1 = Book(1, 'Mockingbird', 'John')
    book2 = Book(1, 'Mockingbird', 'John')

    assert book1 == book2 
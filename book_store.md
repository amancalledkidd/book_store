# Music library Repository Classes Design Recipe


## 1. Design and create the Table

If the table is already created in the database, you can skip this step.

```
# EXAMPLE

Table: books

Columns:
id | title | author_name
```

## 2. Create Test SQL seeds

Your tests will depend on data stored in PostgreSQL to run.

If seed data is provided (or you already created it), you can skip this step.

```sql

```

Run this SQL file on the database to truncate (empty) the table, and insert the seed data. Be mindful of the fact any existing records in the table will be deleted.

```bash
psql -h 127.0.0.1 your_database_name < seeds_{table_name}.sql
```

## 3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name.

```python
# EXAMPLE
# Table name: books

# Model class
class Book


# Repository class
class BookRepository

```

## 4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python
# EXAMPLE
# Table name: books

# Model class


class Book():
    def __init__(self):
        # Fields for row headings
        pass

    def __eq__(self, other):
        # allows object to compare itself to other objects
        pass

    def __repr__(self):
        # returns formmatted string
        pass

        # Replace the attributes by your own columns.


```

*You may choose to test-drive this class, but unless it contains any more logic than the example above, it is probably not needed.*

## 5. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

```python
# EXAMPLE
# Table name: books

# Repository class

class BookRepository():

    # Selecting all books
    # No arguments
    def all(self):
        # Executes the SQL query:
        # SELECT id, title, author_name FROM books;

        # Returns an array of book objects.
        pass

    def find(self, id):
        # Executes the SQL query:
        # SELECT id, title, author_name FROM students WHERE id = $1;

        # Returns a single Student object.
        pass

    def create(self, book):
        # Creates new album and adds it to database
        # Returns None
        pass
    
    def update(self, id):
        pass 

    def delete(self, id):
        pass

```

## 6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

```python
# EXAMPLES

"""
Call instance of book class
check fields are init
"""

book = Book(1, 'Mockingbird', 'John')
book.id # => 1
book.title #=> 'Mockingbird'
book.author_name # => 'John'

"""
Call instance of books
check __repr__ returns formated string of book info
"""

book = Book(1, 'Mockingbird', 'John')
str(book) # => 'Book(1, Mockingbird, 'John')


"""
check __eq__ is works
can compare different instances
"""
book1 = Book(1, 'Mockingbird', 'John')
book2 = Book(1, 'Mockingbird', 'John')

book1 == book2 # => True



repo = BookRepository()

books = repo.all()

len(books) # =>  2

[Book('Nineteen Eighty-Four', 'George Orwell'),
Book('Mrs Dalloway', 'Virginia Woolf'),
Book('Emma', 'Jane Austen'),
Book('Dracula', 'Bram Stoker'),
Book('The Age of Innocence', 'Edith Wharton'),]

# 2
# Get a single student

repo = StudentRepository()

student = repo.find(1)

student.id # =>  1
student.name # =>  'David'
student.cohort_name # =>  'April 2022'

# Add more examples for each method
```

Encode this example as a test.


## 7. Test-drive and implement the Repository class behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->
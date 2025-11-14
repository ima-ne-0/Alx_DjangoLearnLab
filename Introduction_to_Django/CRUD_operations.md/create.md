1. Create Operation

Command: Create a Book instance with the title “1984”, author “George Orwell”, and publication year 1949.

>>> from bookshelf.models import Book
>>> b = Book(title="1984", author="George Orwell", publication_year=1949)
>>> b.save()


# Output: (No output, but the object is successfully created in the database.)
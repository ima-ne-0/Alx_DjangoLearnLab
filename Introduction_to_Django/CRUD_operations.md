CRUD Operations in Django Shell

This file documents the CRUD operations for the Book model of the bookshelf app, as required by the task.

1. Create

Command: Create a Book instance with the title “1984”, author “George Orwell”, and publication year 1949.

>>> from bookshelf.models import Book
>>> b = Book(title="1984", author="George Orwell", publication_year=1949)
>>> b.save()


# Output: (No output, but the object is successfully created in the database.)

2. Retrieve

Command: Retrieve and display all attributes of the book you just created.

>>> b = Book.objects.get(title="1984")
>>> print(b.title, b.author, b.publication_year)


# Output: 1984 George Orwell 1949

3. Update

Command: Update the title of “1984” to “Nineteen Eighty-Four” and save the changes.

>>> b = Book.objects.get(title="1984") # Retrieve the object
>>> b.title = "Nineteen Eighty-Four"
>>> b.save()

# Optional: Verify the update
>>> book_updated = Book.objects.get(publication_year=1949)
>>> print(book_updated.title)


# Output (from verification): Nineteen Eighty-Four

4. Delete

Command: Delete the book you created and confirm the deletion by trying to retrieve all books again.

>>> b = Book.objects.get(title="Nineteen Eighty-Four") # Retrieve the object
>>> b.delete()


# Output: (1, {'bookshelf.Book': 1})

# Confirmation
>>> Book.objects.all()


# Output: <QuerySet []
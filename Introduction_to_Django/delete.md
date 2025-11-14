4. Delete Operation

Command: Delete the book you created and confirm the deletion by trying to retrieve all books again.

>>> b = Book.objects.get(title="Nineteen Eighty-Four")
>>> b.delete()


# Output: (1, {'bookshelf.Book': 1})

# Confirmation
>>> Book.objects.all()


# Output: <QuerySet []
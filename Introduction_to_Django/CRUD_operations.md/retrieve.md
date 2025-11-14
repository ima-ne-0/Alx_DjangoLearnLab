2. Retrieve Operation

Command: Retrieve and display all attributes of the book you just created.

>>> b = Book.objects.get(title="1984")
>>> print(b.title, b.author, b.publication_year)


# Output: 1984 George Orwell 1949
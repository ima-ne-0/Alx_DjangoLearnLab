
>>> from bookshelf.models import Book
>>> b = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> b.save()
>>># Output: (No output, but the object is successfully created in the database.)

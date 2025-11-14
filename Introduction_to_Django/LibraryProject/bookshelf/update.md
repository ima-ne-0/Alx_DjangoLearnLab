3. Update Operation

Command: Update the title of “1984” to “Nineteen Eighty-Four” and save the changes.

>>> b = Book.objects.get(title="1984")
>>> b.title = "Nineteen Eighty-Four"
>>> b.save()


# Output: (No output, but the object is updated successfully.)

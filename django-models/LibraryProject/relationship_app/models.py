from django.db import models

# 1. Author Model (La base)
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 2. Book Model (Relation ForeignKey)
class Book(models.Model):
    title = models.CharField(max_length=200)
    # "Un livre a un auteur"
    # "Un auteur peut avoir PLUSIEURS livres"
    # on_delete=models.CASCADE signifie : si un auteur est supprimé,
    # tous ses livres sont aussi supprimés.
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# 3. Library Model (Relation ManyToMany)
class Library(models.Model):
    name = models.CharField(max_length=100)
    # "Une bibliothèque peut avoir PLUSIEURS livres"
    # "Un livre peut être dans PLUSIEURS bibliothèques"
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

# 4. Librarian Model (Relation OneToOne)
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    # "Un bibliothécaire est assigné à UNE SEULE bibliothèque"
    # "Une bibliothèque a UN SEUL bibliothécaire"
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

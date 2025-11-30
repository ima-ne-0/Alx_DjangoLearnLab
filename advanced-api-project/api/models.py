from django.db import models

# Create your models here.
from django.db import models

class Author(models.Model):
    """
    Le modèle Author représente un auteur de livre.
    Champs :
    - name : Le nom de l'auteur.
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Le modèle Book représente un livre écrit par un auteur.
    Champs :
    - title : Le titre du livre.
    - publication_year : L'année de publication.
    - author : Clé étrangère liant le livre à un auteur.
    
    Relation :
    Un auteur peut avoir plusieurs livres (One-to-Many).
    L'argument 'related_name="books"' nous permet d'accéder aux livres d'un auteur
    via l'attribut .books (ex: author_instance.books.all()).
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

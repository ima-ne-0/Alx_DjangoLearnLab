from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    """
    BookSerializer gère la sérialisation du modèle Book.
    Il inclut une validation personnalisée pour l'année de publication.
    """
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """
        Vérifie que l'année de publication n'est pas dans le futur.
        """
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("L'année de publication ne peut pas être dans le futur.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    AuthorSerializer gère la sérialisation du modèle Author.
    Il inclut une relation imbriquée (nested) pour afficher les livres associés.
    """
    # Ici, nous imbriquons le BookSerializer.
    # many=True indique qu'il s'agit d'une liste d'objets.
    # read_only=True signifie que nous ne créons pas de livres directement via l'auteur ici.
    # La source est automatiqument trouvée grâce au 'related_name="books"' dans models.py
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
from django.contrib import admin
from .models import Book

# On crée une classe pour personnaliser l'affichage
class BookAdmin(admin.ModelAdmin):
    # Tâche 2.1: Affiche ces champs dans la liste
    list_display = ('title', 'author', 'publication_year')

    # Tâche 2.2: Ajoute une barre de recherche pour ces champs
    search_fields = ('title', 'author')

    # Tâche 2.2: Ajoute un filtre sur le côté
    list_filter = ('publication_year', 'author')

# On enregistre le modèle Book AVEC sa classe de personnalisation
admin.site.register(Book, BookAdmin)

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Tâche 1: Vue basée sur une fonction (FBV) pour lister tous les livres

def book_list(request):
    """
    Récupère tous les objets Book de la base de données et
    les transmet au template list_books.html.
    """
    # On utilise .select_related('author') pour optimiser la requête
    # en récupérant les auteurs en même temps que les livres.
    books = Book.objects.select_related('author').all()
    
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)


# Tâche 2: Vue basée sur une classe (CBV) pour les détails d'une bibliothèque

class LibraryDetailView(DetailView):
    """
    Affiche les détails d'un objet Library spécifique.
    Django s'occupe de :
    1. Récupérer l'objet Library par son 'pk' (clé primaire) depuis l'URL.
    2. Le transmettre au template 'library_detail.html'.
    3. Le nom par défaut de l'objet dans le template est 'library' (ou 'object').
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library' # Rend l'objet disponible en tant que 'library'

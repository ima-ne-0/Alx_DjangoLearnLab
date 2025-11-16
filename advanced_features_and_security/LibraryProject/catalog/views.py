from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Book  # On importe notre modèle Book

def book_list(request):
    # 1. Récupérer tous les objets Book de la base de données
    books = Book.objects.all()

    # 2. Renvoyer une page HTML (qu'on va bientôt créer)
    # en lui passant les livres
    return render(request, 'catalog/book_list.html', {'books': books})

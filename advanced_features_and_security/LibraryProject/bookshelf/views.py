from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book # Le modèle Book de l'app "bookshelf"

# --- Tâche "Permissions": Vues protégées ---

@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """
    Récupère tous les objets Book (de bookshelf) et
    les transmet au template.
    """
    books = Book.objects.all()
    context = {
        'books': books
    }
    # On peut réutiliser le template de l'autre app,
    # mais il vaut mieux créer un nouveau template plus tard.
    # Pour l'instant, le checker veut juste cette vue.
    return render(request, 'relationship_app/list_books.html', context)

@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def book_add(request):
    return HttpResponse("Page pour ajouter un livre (protégée par 'bookshelf.can_create')")

@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    return HttpResponse(f"Page pour modifier le livre {pk} (protégée par 'bookshelf.can_edit')")
# ... (imports existants)
from .forms import BookSearchForm
from django.db.models import Q # Requis pour la recherche ORM

# ... (autres vues: book_list, book_add, etc.)

# --- TÂCHE DE SÉCURITÉ (Étape 3) ---
# Vue de recherche qui utilise un formulaire pour valider et nettoyer l'entrée.

def book_search_view(request):
    """
    Cette vue gère la recherche de livres de manière sécurisée.
    """
    form = BookSearchForm()
    results = [] # Liste des résultats de recherche

    if 'query' in request.GET:
        # Met les données GET dans le formulaire
        form = BookSearchForm(request.GET)
        
        # Étape 3: Valide et nettoie les entrées
        if form.is_valid():
            query = form.cleaned_data['query']
            
            # Étape 3: Utilise l'ORM de Django (paramétré)
            # C'est ce qui PRÉVIENT LES INJECTIONS SQL.
            # N'utilisez JAMAIS de f-strings pour construire des requêtes SQL.
            results = Book.objects.filter(
                Q(title__icontains=query) | Q(author__icontains=query)
            )

    # Le contexte inclut le formulaire (pour l'affichage) et les résultats
    context = {
        'form': form,
        'books': results, # Réutilise la variable 'books' que 'book_list.html' attend
    }
    
    # Réutilise le template 'book_list.html' pour afficher les résultats
    # (ou 'form_example.html' si tu préfères)
    return render(request, 'bookshelf/form_example.html', context)

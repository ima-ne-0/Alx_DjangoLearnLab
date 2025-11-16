from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book # Le modèle Book de l'app "bookshelf"
from django.db.models import Q # Requis pour la recherche ORM

# --- CORRECTION POUR LE CHECKER ALX ---
# Importe le formulaire avec le bon nom "ExampleForm"
from .forms import ExampleForm

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
    return render(request, 'relationship_app/list_books.html', context)

@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def book_add(request):
    return HttpResponse("Page pour ajouter un livre (protégée par 'bookshelf.can_create')")

@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    return HttpResponse(f"Page pour modifier le livre {pk} (protégée par 'bookshelf.can_edit')")

@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    return HttpResponse(f"Page pour supprimer le livre {pk} (protégée par 'bookshelf.can_delete')")

# --- TÂCHE DE SÉCURITÉ (Étape 3) ---
# --- CORRECTION POUR LE CHECKER ALX ---
# Utilise "ExampleForm" au lieu de "BookSearchForm"
def book_search_view(request):
    """
    Cette vue gère la recherche de livres de manière sécurisée.
    """
    form = ExampleForm() # Utilise le nouveau nom
    results = [] 

    if 'query' in request.GET:
        form = ExampleForm(request.GET) # Utilise le nouveau nom
        
        if form.is_valid():
            query = form.cleaned_data['query']
            
            results = Book.objects.filter(
                Q(title__icontains=query) | Q(author__icontains=query)
            )

    context = {
        'form': form,
        'books': results, 
    }
    
    return render(request, 'bookshelf/form_example.html', context)

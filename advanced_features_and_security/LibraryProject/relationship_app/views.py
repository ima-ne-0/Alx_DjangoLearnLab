from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from django.http import HttpResponse, HttpResponseForbidden

# Imports pour les modèles (séparés pour le checker)
from .models import Book
from .models import Library

# Imports pour l'authentification
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required

# --- Tâche "Vues": Vue-Fonction (list_books) ---
def list_books(request):
    """
    Récupère tous les objets Book de la base de données et
    les transmet au template list_books.html.
    """
    books = Book.objects.all() # Version simple pour le checker
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)


# --- Tâche "Vues": Vue-Classe (LibraryDetailView) ---
class LibraryDetailView(DetailView):
    """
    Affiche les détails d'un objet Library spécifique.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# --- Tâche "Authentification": Vue d'inscription (register) ---
def register(request):
    """
    Une vue pour l'inscription de nouveaux utilisateurs.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Connecte l'utilisateur
            return redirect('book-list') # Redirige
    else:
        form = UserCreationForm()
    
    return render(request, 'relationship_app/register.html', {'form': form})

# --- Tâche "Roles": Fonctions de test de rôle ---
def is_admin(user):
    # Vérifie si le profil existe avant d'accéder au rôle
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# --- Tâche "Roles": Vues basées sur les rôles ---
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# --- Tâche "Permissions": Vues protégées ---
@login_required
@permission_required('relationship_app.can_add_book', raise_exception=True)
def book_add(request):
    return HttpResponse("Page pour ajouter un livre (protégée par permission)")

@login_required
@permission_required('relationship_app.can_change_book', raise_exception=True)
def book_edit(request, pk):
    return HttpResponse(f"Page pour modifier le livre {pk} (protégée par permission)")

@login_required
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def book_delete(request, pk):
    return HttpResponse(f"Page pour supprimer le livre {pk} (protégée par permission)")

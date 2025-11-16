# Ce fichier est NOUVEAU. Il gère les routes pour "relationship_app".

from django.urls import path
from . import views

urlpatterns = [
    # Route pour ta vue-fonction (FBV)
    path('books/', views.book_list, name='book-list'),
    
    # Route pour ta vue-classe (CBV)
    # <int:pk> capture le numéro ID de la bibliothèque depuis l'URL
    # et le transmet automatiquement à la DetailView.
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),
]
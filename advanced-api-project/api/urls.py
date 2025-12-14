from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)

urlpatterns = [
    # Route pour lister tous les livres (GET /books/)
    path('books/', BookListView.as_view(), name='book-list'),

    # Route pour voir un livre spécifique (GET /books/1/)
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Route pour créer un livre (POST /books/create/)
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # Route pour modifier un livre (PUT/PATCH /books/update/1/)
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),

    # Route pour supprimer un livre (DELETE /books/delete/1/)
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
]
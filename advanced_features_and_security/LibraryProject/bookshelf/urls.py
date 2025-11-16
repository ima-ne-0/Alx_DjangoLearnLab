from django.urls import path
from . import views # Importe les vues de bookshelf

urlpatterns = [
    # Routes pour les vues protégées par permission
    path('list/', views.book_list, name='book-list-bookshelf'),
    path('add/', views.book_add, name='book-add-bookshelf'),
    path('<int:pk>/edit/', views.book_edit, name='book-edit-bookshelf'),
    path('<int:pk>/delete/', views.book_delete, name='book-delete-bookshelf'),
    path('search/', views.book_search_view, name='book-search-bookshelf'),
]

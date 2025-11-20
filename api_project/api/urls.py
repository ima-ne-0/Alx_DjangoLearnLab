from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Création du routeur
router = DefaultRouter()
# On enregistre notre ViewSet
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route existante pour la liste simple
    path('books/', BookList.as_view(), name='book-list'),

    # Inclusion des URLs générées par le routeur pour le CRUD complet
    path('', include(router.urls)),
]

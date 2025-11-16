from django.urls import path
from . import views  # On importe les vues (views.py) de ce dossier

urlpatterns = [
    # Quand quelqu'un arrive à la racine de cette app,
    # montre-lui la vue "book_list"
    path("", views.book_list, name="book_list"),
]
from django.urls import path
from .views import list_books, LibraryDetailView, register # Ajoute 'register'
from django.contrib.auth import views as auth_views # Importe les vues d'authentification

urlpatterns = [
    # Tes anciennes routes de l'app
    path('books/', list_books, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    
    # --- AJOUTE CES NOUVELLES ROUTES ---
    
    # Login: Utilise la vue LoginView intégrée de Django
    # On lui dit quel template utiliser
    path('login/', auth_views.LoginView.as_view(
        template_name='relationship_app/login.html'
    ), name='login'),
    
    # Logout: Utilise la vue LogoutView intégrée de Django
    # On lui dit quel template utiliser
    path('logout/', auth_views.LogoutView.as_view(
        template_name='relationship_app/logout.html'
    ), name='logout'),
    
    # Register: Utilise notre vue "register" personnalisée
    path('register/', register, name='register'),
]

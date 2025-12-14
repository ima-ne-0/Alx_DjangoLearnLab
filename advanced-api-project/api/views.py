from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework
from rest_framework import filters
from .models import Book
from .serializers import BookSerializer

# Étape 1 : ListView pour récupérer tous les livres
class BookListView(generics.ListAPIView):
    """
    Vue pour lister tous les livres.
    Type : GenericAPIView (ListAPIView)
    Comportement : GET seulement.
    Permissions : Accessible à tout le monde (lecture seule).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Étape 3 : Intégration de filtres de base (ex: recherche ou ordre)
    # Ici, nous laissons le comportement par défaut mais on pourrait ajouter filter_backends
    permission_classes = [IsAuthenticatedOrReadOnly] 
    # Note: IsAuthenticatedOrReadOnly autorise tout le monde à lire (GET)
    filter_backends = [
        rest_framework.DjangoFilterBackend, # Pour le filtrage exact (Step 1)
        filters.SearchFilter,               # Pour la recherche textuelle (Step 2)
        filters.OrderingFilter              # Pour le tri (Step 3)
    ]
    # Step 1: Champs de filtrage (égalité exacte)
    # Permet de faire: /books/?publication_year=2024
    filterset_fields = ['title', 'author', 'publication_year']

    # Step 2: Champs de recherche (texte partiel)
    # Permet de faire: /books/?search=Harry
    # Note: 'author__name' permet de chercher sur le nom de l'auteur via la relation ForeignKey
    search_fields = ['title', 'author__name']

    # Step 3: Champs de tri
    # Permet de faire: /books/?ordering=publication_year
    ordering_fields = ['title', 'publication_year']
    
    # Tri par défaut (optionnel mais recommandé)
    ordering = ['title']

# Étape 1 : DetailView pour récupérer un livre par son ID
class BookDetailView(generics.RetrieveAPIView):
    """
    Vue pour récupérer les détails d'un livre spécifique par son ID.
    Type : GenericAPIView (RetrieveAPIView)
    Comportement : GET seulement.
    Permissions : Accessible à tout le monde.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Étape 1 : CreateView pour créer un nouveau livre
class BookCreateView(generics.CreateAPIView):
    """
    Vue pour créer un nouveau livre.
    Type : GenericAPIView (CreateAPIView)
    Comportement : POST seulement.
    Permissions : Authentifié seulement (IsAuthenticated).
    Validation : Gérée automatiquement par le BookSerializer.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Étape 4 : Protection

    # Étape 3 : Personnalisation du comportement
    def perform_create(self, serializer):
        # Exemple de personnalisation : on pourrait ajouter une logique ici
        # avant de sauvegarder, comme loguer l'utilisateur qui a créé le livre.
        serializer.save()

# Étape 1 : UpdateView pour modifier un livre existant
class BookUpdateView(generics.UpdateAPIView):
    """
    Vue pour mettre à jour un livre existant.
    Type : GenericAPIView (UpdateAPIView)
    Comportement : PUT/PATCH.
    Permissions : Authentifié seulement.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# Étape 1 : DeleteView pour supprimer un livre
class BookDeleteView(generics.DestroyAPIView):
    """
    Vue pour supprimer un livre.
    Type : GenericAPIView (DestroyAPIView)
    Comportement : DELETE.
    Permissions : Authentifié seulement.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
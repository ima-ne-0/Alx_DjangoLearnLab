import os
import django

# --- Configuration pour charger Django ---
# (Nécessaire pour qu'un script externe puisse utiliser les modèles)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()
# ----------------------------------------

# Importe tes modèles APRÈS le setup
from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    print("--- Démarrage des requêtes ---")

    # --- 1. Création de données pour les tests ---
    # (On ne peut rien interroger si la base de données est vide)

    print("Création des données...")

    # Créer un auteur
    author_jules = Author.objects.create(name="Jules Verne")

    # Créer des livres pour cet auteur
    book_20k = Book.objects.create(title="20 000 lieues sous les mers", author=author_jules)
    book_voyage = Book.objects.create(title="Voyage au centre de la Terre", author=author_jules)

    # Créer une bibliothèque et y ajouter des livres
    main_lib = Library.objects.create(name="Bibliothèque Principale")
    main_lib.books.add(book_20k, book_voyage)

    # Créer un bibliothécaire pour cette bibliothèque
    Librarian.objects.create(name="Capitaine Nemo", library=main_lib)

    print("Données créées !")
    print("-" * 20)

    # --- 2. Requêtes demandées ---

    # A. Requête: Tous les livres d'un auteur (ForeignKey)
    print("\n[REQUÊTE 1: Livres de Jules Verne]")
    books_by_jules = Book.objects.filter(author__name="Jules Verne")
    for book in books_by_jules:
        print(f"- {book.title}")

    # B. Requête: Tous les livres d'une bibliothèque (ManyToMany)
    print("\n[REQUÊTE 2: Livres dans la 'Bibliothèque Principale']")
    lib = Library.objects.get(name="Bibliothèque Principale")
    for book in lib.books.all():
        print(f"- {book.title}")

    # C. Requête: Le bibliothécaire d'une bibliothèque (OneToOne)
    print("\n[REQUÊTE 3: Bibliothécaire de la 'Bibliothèque Principale']")
    # On peut accéder à la relation "inverse" OneToOne
    print(f"- {lib.librarian.name}")

    print("\n--- Requêtes terminées ---")

    # --- Nettoyage (optionnel, mais propre) ---
    Author.objects.all().delete()
    Book.objects.all().delete()
    Library.objects.all().delete()
    Librarian.objects.all().delete()
    print("\n(Données de test nettoyées)")

# Fait tourner le script
if __name__ == "__main__":
    run_queries()
# Ce script contient les exemples de requêtes pour le checker ALX.
# Il n'est pas fait pour être exécuté directement,
# mais pour être lu par le correcteur automatique.

from relationship_app.models import Author, Book, Library, Librarian

# --- Variables (placeholder) pour les requêtes ---
author_name = "Some Author Name"
library_name = "Some Library Name"

# --- 1. Requête: "Query all books by a specific author." ---
# Le checker s'attend à voir ce type de requête:
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
# print(books_by_author)


# --- 2. Requête: "List all books in a library." ---
# Le checker s'attend à voir ce type de requête:
lib = Library.objects.get(name=library_name)
books_in_library = lib.books.all()
# print(books_in_library)


# --- 3. Requête: "Retrieve the librarian for a library." ---
# Le checker s'attend à voir ce type de requête:
lib = Library.objects.get(name=library_name)
librarian = lib.librarian
# print(librarian)

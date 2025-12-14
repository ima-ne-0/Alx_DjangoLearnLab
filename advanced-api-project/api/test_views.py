from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITests(APITestCase):
    """
    Classe de test pour les endpoints de l'API Book.
    Teste les opérations CRUD, les permissions et les fonctionnalités de filtrage/recherche.
    """

    def setUp(self):
        """
        Cette méthode s'exécute avant CHAQUE test.
        Elle prépare un environnement propre : un utilisateur, un auteur et un livre.
        """
        self.user = User.objects.create_user(username='testuser', password='password')
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(
            title="Harry Potter and the Philosopher's Stone",
            publication_year=1997,
            author=self.author
        )
        self.list_url = reverse('book-list')
        self.client.login(username='testuser', password='password')

    def test_create_book_authenticated(self):
        """
        Vérifie qu'un utilisateur authentifié peut créer un livre.
        """
        data = {
            "title": "Harry Potter and the Chamber of Secrets",
            "publication_year": 1998,
            "author": self.author.id
        }
        url = reverse('book-create')
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(response.data['title'], "Harry Potter and the Chamber of Secrets")

    def test_create_book_unauthenticated(self):
        """
        Vérifie qu'un utilisateur NON authentifié NE PEUT PAS créer un livre.
        """
        self.client.logout()
        data = {
            "title": "Unauthorized Book",
            "publication_year": 2023,
            "author": self.author.id
        }
        url = reverse('book-create')
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        """
        Vérifie la mise à jour d'un livre existant.
        """
        url = reverse('book-update', args=[self.book.id])
        data = {
            "title": "Harry Potter Updated",
            "publication_year": 1997,
            "author": self.author.id
        }
        response = self.client.put(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Harry Potter Updated")

    def test_delete_book(self):
        """
        Vérifie la suppression d'un livre.
        """
        url = reverse('book-delete', args=[self.book.id])
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        """
        Teste le filtrage par année de publication.
        """
        Book.objects.create(title="Old Book", publication_year=1900, author=self.author)
        response = self.client.get(self.list_url + '?publication_year=1997')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Harry Potter and the Philosopher's Stone")

    def test_search_books(self):
        """
        Teste la fonctionnalité de recherche.
        """
        Book.objects.create(title="Learning Python", publication_year=2020, author=self.author)
        response = self.client.get(self.list_url + '?search=Python')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Learning Python")

    def test_ordering_books(self):
        """
        Teste le tri des résultats.
        """
        Book.objects.create(title="A Book", publication_year=2021, author=self.author)
        Book.objects.create(title="Z Book", publication_year=2022, author=self.author)
        
        response = self.client.get(self.list_url + '?ordering=title')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "A Book")
        self.assertEqual(response.data[-1]['title'], "Z Book")
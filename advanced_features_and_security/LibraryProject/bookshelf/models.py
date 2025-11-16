from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# --- ÉTAPE 3: Custom User Manager ---
class CustomUserManager(BaseUserManager):
    """
    Manager personnalisé pour notre modèle CustomUser.
    """
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)

# --- ÉTAPE 1: Custom User Model ---
class CustomUser(AbstractUser):
    """
    Modèle utilisateur personnalisé qui étend AbstractUser.
    """
    username = None 
    email = models.EmailField('email address', unique=True)

    # Champs personnalisés demandés
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

# --- ANCIEN MODÈLE "Book" de l'app "bookshelf" ---
# (Il doit rester ici)
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title

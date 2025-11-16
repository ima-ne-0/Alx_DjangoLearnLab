from django.db import models
# --- ÉTAPE 1: Imports pour le Custom User ---
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

# --- ÉTAPE 3: Custom User Manager ---

class CustomUserManager(BaseUserManager):
    """
    Manager personnalisé pour notre modèle CustomUser.
    """
    def create_user(self, email, password=None, **extra_fields):
        """
        Crée et sauvegarde un utilisateur avec un email et un mot de passe.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Crée et sauvegarde un superutilisateur.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


# --- ÉTAPE 1 (suite): Custom User Model ---

class CustomUser(AbstractUser):
    """
    Modèle utilisateur personnalisé qui étend AbstractUser.
    On utilise l'email comme champ de connexion principal.
    """
    # On enlève 'username' en le mettant à None
    username = None 
    email = models.EmailField('email address', unique=True)

    # Champs personnalisés demandés
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    # Dit à Django d'utiliser 'email' pour se connecter
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Enlève 'email' des champs requis (car c'est le username)

    # Lie le manager personnalisé
    objects = CustomUserManager()

    def __str__(self):
        return self.email


# --- ÉTAPE 7: Mettre à jour les modèles existants ---

class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )
    
    # --- MODIFICATION IMPORTANTE ---
    # Ne se lie plus à 'User', mais à notre 'CustomUser'
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.email} - {self.role}"

# --- MODIFICATION IMPORTANTE (Signaux) ---
# Le 'sender' est maintenant notre CustomUser
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


# --- ANCIENS MODÈLES (doivent rester pour que le projet fonctionne) ---

class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    class Meta:
        permissions = (
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        )
    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

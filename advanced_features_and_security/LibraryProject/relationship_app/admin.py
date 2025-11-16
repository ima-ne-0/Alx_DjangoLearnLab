from django.contrib import admin

# Register your models here.
from django.contrib import admin
# --- AJOUTE CES IMPORTS ---
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserProfile, Author, Book, Library, Librarian

# --- ÉTAPE 4: Admin pour le CustomUser ---
class CustomUserAdmin(UserAdmin):
    """
    Configure l'affichage de notre CustomUser dans l'admin.
    """
    model = CustomUser
    list_display = ['email', 'is_staff', 'is_active', 'date_of_birth']
    
    # Utilise les fieldsets de UserAdmin et ajoute les nôtres
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    
    search_fields = ['email']
    ordering = ['email']

# Enregistre le CustomUser avec sa config personnalisée
admin.site.register(CustomUser, CustomUserAdmin)

# --- Le reste de tes enregistrements admin ---
admin.site.register(UserProfile)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)

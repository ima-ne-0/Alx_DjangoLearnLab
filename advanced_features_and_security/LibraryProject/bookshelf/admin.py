from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book # Importe les modèles de cette app

# --- Admin pour le CustomUser ---
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'is_staff', 'is_active', 'date_of_birth']
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    search_fields = ['email']
    ordering = ['email']

# Enregistre les modèles de cette app
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book) # Le modèle Book de l'app bookshelf

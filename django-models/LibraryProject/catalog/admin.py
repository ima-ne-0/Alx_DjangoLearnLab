from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book  # Importe ton modèle

# Enregistre-le
admin.site.register(Book)

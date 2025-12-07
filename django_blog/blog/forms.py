from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Import obligatoire pour ALX :
from taggit.forms import TagWidget
from .models import Post, Comment

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            # AJOUT OBLIGATOIRE POUR LE ROBOT ALX :
            'tags': TagWidget(attrs={'class': 'form-control', 'placeholder': 'Tags (séparés par des virgules)'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Votre commentaire...'}),
        }

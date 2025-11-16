from django import forms

class BookSearchForm(forms.Form):
    """
    Un formulaire simple pour valider une requête de recherche.
    Utiliser un Form garantit que l'entrée est un CharField
    et non un code malveillant.
    """
    query = forms.CharField(
        max_length=100,
        required=True,
        label="Search for a book"
    )

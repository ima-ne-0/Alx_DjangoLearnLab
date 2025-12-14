from django import forms

# --- CORRECTION POUR LE CHECKER ALX ---
# Renommage de "BookSearchForm" en "ExampleForm"
class ExampleForm(forms.Form):
    """
    Un formulaire simple pour valider une requête de recherche.
    """
    query = forms.CharField(
        max_length=100,
        required=True,
        label="Search for a book"
    )

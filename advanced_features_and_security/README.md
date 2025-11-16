# Documentation du Projet "Advanced Features and Security"

Ce projet met en œuvre un contrôle d'accès avancé dans Django.

## 1. Rôles (Roles)

Les rôles sont gérés par le modèle `UserProfile` dans `relationship_app/models.py`.
Chaque utilisateur se voit attribuer un `UserProfile` avec l'un des rôles suivants :
* Admin
* Librarian
* Member

L'accès aux vues spécifiques aux rôles (`admin_view`, `librarian_view`) est contrôlé par le décorateur `@user_passes_test` dans `relationship_app/views.py`.

## 2. Permissions de Groupe

Ce projet utilise des permissions personnalisées au niveau du modèle.

**Modèle :** `relationship_app.Book`

**Permissions (définies dans `models.py`) :**
* `can_view`: Peut voir la liste des livres.
* `can_create`: Peut accéder à la page pour ajouter un livre.
* `can_edit`: Peut accéder à la page pour modifier un livre.
* `can_delete`: Peut accéder à la page pour supprimer un livre.

**Mise en œuvre (dans `views.py`) :**
Ces permissions sont vérifiées à l'aide du décorateur `@permission_required`.

**Configuration (via `/admin/`) :**
1.  Créer des **Groupes** (ex: "Editors", "Viewers").
2.  Assigner les permissions (ex: `relationship_app | book | Can view book`) à ces groupes.
3.  Assigner les **Utilisateurs** (`CustomUser`) aux groupes appropriés pour leur donner accès.

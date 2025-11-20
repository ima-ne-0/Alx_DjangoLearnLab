# Rapport de Sécurité et Déploiement

Ce document détaille les mesures de sécurité implémentées dans le projet, conformément aux tâches ALX.

## 1. Mesures de Sécurité Implémentées

### Fichier: `settings.py`

Tous les paramètres de sécurité sont configurés dans `LibraryProject/settings.py`.

* **`X_FRAME_OPTIONS = 'DENY'`**: (Tâche 3) Protège contre le "clickjacking" en empêchant le site d'être chargé dans un `<iframe>`.
* **`SECURE_CONTENT_TYPE_NOSNIFF = True`**: (Tâche 3) Empêche le navigateur de faire du "MIME-sniffing", forçant le respect du `Content-Type` déclaré et réduisant les risques XSS.
* **`SECURE_BROWSER_XSS_FILTER = True`**: (Tâche 3) Active le filtre XSS du navigateur.

### Paramètres HTTPS (Prêts pour la Production)

Les paramètres suivants sont configurés mais **commentés** pour permettre le développement local en HTTP. En production (HTTPS), ils seraient activés.

* **`SECURE_SSL_REDIRECT = True`**: (Tâche 1) Redirige automatiquement tout le trafic HTTP vers HTTPS.
* **`SESSION_COOKIE_SECURE = True`**: (Tâche 2) Garantit que les cookies de session ne sont envoyés que via des connexions HTTPS.
* **`CSRF_COOKIE_SECURE = True`**: (Tâche 2) Garantit que les cookies CSRF ne sont envoyés que via des connexions HTTPS.
* **`SECURE_HSTS_SECONDS`**: (Tâche 1) Active HSTS pour forcer les navigateurs à utiliser HTTPS pour une période donnée.

### Fichiers `views.py` et `templates`

* **CSRF (Tâche 2)**: Tous les formulaires `POST` (comme `register.html` et `login.html`) incluent le tag `{% csrf_token %}` pour prévenir les attaques Cross-Site Request Forgery.
* **Injection SQL (Tâche 3)**: Toutes les requêtes de base de données (comme la recherche dans `bookshelf/views.py`) utilisent l'ORM de Django (`Book.objects.filter(...)`) au lieu de concaténations de chaînes. L'ORM paramètre automatiquement les requêtes, ce qui neutralise les attaques par injection SQL.
* **Validation des entrées (Tâche 3)**: Les entrées utilisateur sont validées à l'aide de `django.forms.Form` (ex: `ExampleForm`), ce qui garantit que les données sont nettoyées avant d'être utilisées.

## 2. Configuration de Déploiement (Tâche 4)

Pour que les paramètres HTTPS (SSL) fonctionnent, l'application doit être déployée derrière un serveur web de production (comme Nginx ou Apache) et un certificat SSL doit être installé.

**Exemple de flux de travail pour le déploiement :**
1.  **Serveur d'application**: Utiliser `Gunicorn` pour faire tourner l'application Django.
2.  **Serveur Web (Reverse Proxy)**: Utiliser `Nginx` pour recevoir les requêtes des utilisateurs (port 80 et 443) et les transmettre à Gunicorn.
3.  **Certificat SSL**: Utiliser `Let's Encrypt` (via `Certbot`) pour obtenir un certificat SSL gratuit pour le domaine.
4.  **Configuration Nginx**: Nginx serait configuré pour :
    * Servir les fichiers statiques (`static/`) et médias (`media/`).
    * Rediriger tout le trafic du port 80 (HTTP) vers le port 443 (HTTPS).
    * Transmettre les requêtes HTTPS à Gunicorn.
5.  **Activation des paramètres Django**: Une fois Nginx et SSL configurés, la variable d'environnement `DEBUG` serait mise à `False`, et les paramètres `SECURE_SSL_REDIRECT`, `SESSION_COOKIE_SECURE`, et `CSRF_COOKIE_SECURE` seraient mis à `True` dans `settings.py`.

# LITRevu - Plateforme de critiques littéraires

LITRevu est une application web Django permettant à une communauté d'utilisateurs de demander des critiques de livres ou d'articles (Tickets) et d'y répondre (Critiques), tout en gérant un système d'abonnement pour filtrer leur flux d'actualité.

## Fonctionnalités principales

* **Authentification sécurisée** : Inscription, connexion et déconnexion.
* **Gestion des Tickets et Critiques** : Création, modification et suppression (opérations CRUD limitées aux auteurs).
* **Création combinée** : Possibilité de publier simultanément un ticket et sa critique associée.
* **Système d'abonnement (Followers)** : Suivre d'autres utilisateurs pour voir leurs publications dans le flux principal.
* **Flux d'actualité personnalisé (Feed)** : Affichage chronologique des publications de l'utilisateur et des personnes qu'il suit.
* **Interface UI/UX** : Design épuré, responsive et conforme aux maquettes fournies.

## Prérequis

* Python 3.10 ou supérieur
* pip (gestionnaire de paquets Python)
* Git

## Installation et exécution locale

Suivez ces étapes pour lancer le projet sur votre machine locale.

> **Note :** Selon votre système d'exploitation et votre configuration, remplacez `python` par `python3` dans les commandes ci-dessous si nécessaire (notamment sur macOS / Linux).

### 1. Cloner le dépôt

```bash
git clone https://github.com/alanhuet/OC---P9---LITRevu.git
cd OC---P9---LITRevu
```

### 2. Créer et activer l'environnement virtuel
**Sur Windows :**

```bash
python -m venv env
env\Scripts\activate
```

**Sur macOS / Linux :**

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Initialiser la base de données (SQLite)

```bash
python manage.py migrate
```

### 5. (Optionnel) Créer un compte administrateur / superutilisateur
Pour accéder à l'interface d'administration Django (http://127.0.0.1:8000/admin/) :

```bash
python manage.py createsuperuser
```

### 6. Lancer le serveur de développement

```bash
python manage.py runserver
```

L'application est maintenant accessible via votre navigateur à l'adresse suivante : http://127.0.0.1:8000

Technologies utilisées
Backend : Python, Django 6.1

Frontend : HTML5, CSS3

Base de données : SQLite (par défaut pour le développement)

Traitement d'images : Pillow (gestion du redimensionnement)

Auteur
Alan Huet - Projet étudiant pour OpenClassrooms
# Content-based Image Retrieval System

Ce projet implémente un système de recherche d'images basé sur le contenu en utilisant Streamlit pour l'interface utilisateur. Il utilise des descripteurs d'images et diverses fonctions de distance pour comparer une image téléchargée avec un jeu de données d'images pré-calculées.

## Structure du Projet

- `app.py` : Fichier principal pour l'interface utilisateur Streamlit.
- `data_processing.py` : Script pour traiter les jeux de données d'images et calculer les signatures.
- `descriptor.py` : Implémentation des descripteurs d'images.
- `distance.py` : Fonctions de calcul des distances entre les descripteurs.
- `images` : Dossier contenant les images du jeu de données.

## Prérequis

- Python 3.x
- Streamlit
- NumPy
- OpenCV
- scikit-image
- Pillow

Installez les dépendances avec :

```bash
pip install -r requirements.txt
Utilisation
Étape 1 : Prétraitement des Images
Avant d'utiliser l'application Streamlit, il est nécessaire de prétraiter les images et de calculer leurs signatures. Pour cela, exécutez le script data_processing.py :

bash
Copier le code
python data_processing.py
Ce script génère les fichiers signatures_glcm.npy et signatures_bitdesc.npy qui contiennent les signatures des images.

Étape 2 : Lancer l'Application Streamlit
Après avoir prétraité les images, lancez l'application Streamlit :

bash
Copier le code
streamlit run app.py
Étape 3 : Utilisation de l'Interface
Téléversez une image en utilisant l'interface.
Sélectionnez le descripteur (GLCM ou BIT) et la fonction de distance (Manhattan, Euclidean, Chebyshev, Canberra) depuis la barre latérale.
Indiquez le nombre d'images similaires à afficher.
L'application affichera les images les plus similaires du jeu de données.
Détails des Fichiers
app.py
Ce fichier contient le code pour l'interface utilisateur. Il permet de téléverser une image, de sélectionner les paramètres, et d'afficher les images similaires à partir du jeu de données.

data_processing.py
Ce script traite les images du dossier images, calcule leurs descripteurs et enregistre les signatures dans des fichiers .npy.

descriptor.py
Ce fichier implémente deux fonctions de descripteurs d'images :

glcm : Utilise la matrice de cooccurrence de niveaux de gris (Gray-Level Co-occurrence Matrix).
bitdesc : Utilise le descripteur BiT (Bio-Inspired Texture).
distance.py
Ce fichier contient les fonctions de calcul des distances entre les descripteurs :

manhattan
euclidean
chebyshev
canberra
Dossier d'Images
Le dossier images doit contenir les images du jeu de données organisées en sous-dossiers si nécessaire.

Acknowledgements
Ce projet a été réalisé en utilisant diverses bibliothèques open-source. Un grand merci à leurs développeurs.

License
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

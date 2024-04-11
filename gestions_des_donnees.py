import os
import cv2
import pandas as pd

class Gestions_des_donnees():
    def __init__(self):
        """Cette fonction va s'occuper de la gestion des données, le chargement et l'enrégistrement.
        """
    
    def lire_les_images(self, chemin_dossier: str, noms_des_fichiers: list[str], taille_image=64):
        """Cette fonction permet de lire des images et de les redimensionnées à la taille taille_image.

        Args:
            chemin_dossier (str): Le chemin du dossier
            noms_des_fichiers (list[str]): Les noms des fichiers qui doivent être charger.
            
        return: 
            list[np.ndarray]: Renvoie une liste des images dans des tableaux numpy.
        """
        
        # Association des noms des fichiers avec les extensions de format pour image.
        fichiers_a_charger = [str(nom_fichier) + '.jpg' for nom_fichier in noms_des_fichiers]
        
        # Liste des noms de fichiers d'images dans le répertoire
        chemins_des_images = [fichier for fichier in os.listdir(chemin_dossier) if fichier in fichiers_a_charger]
        
        # Lecture des images dans une liste.
        donnees = []
        for nom_du_fichier in chemins_des_images:
            chemin_du_fichier = os.path.join(chemin_dossier, nom_du_fichier)
            image = cv2.imread(chemin_du_fichier)
            image = cv2.resize(image, (taille_image, taille_image), interpolation=cv2.INTER_AREA)
            donnees.append(image)
        
        if len(donnees) != len(noms_des_fichiers): 
            raise Exception("Une erreur s'est produite lors de la lecture des fichiers, toutes les images n'ont pas été trouvées. !!!")
        
        # Création d'un DataFrame à partir de la liste des images
        return donnees
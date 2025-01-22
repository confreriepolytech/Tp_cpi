#Ceci est un programme test
#utf-8

import tkinter as tk
from tkinter import simpledialog

# Fonction pour recuperer les titres et sous-titres
def recuperer_titres_sous_titres():
    # Demander a l'utilisateur de saisir les titres et sous-titres
    titres = simpledialog.askstring("Saisie des titres", "Veuillez entrer les titres et sous-titres :")
    return titres

# Fonction pour ecrire les titres et sous-titres dans le fichier
def ecrire_dans_fichier(fichier, contenu):
    with open(fichier, 'a') as f:
        f.write(contenu + '\n')

# Nom du fichier
nom_fichier = "Cahier de texte.txt"

# Creer l'interface graphique pour la boite de dialogue
root = tk.Tk()
root.withdraw()  # Masquer la fenetre principale

# Recuperer les titres et sous-titres
titres_sous_titres = recuperer_titres_sous_titres()

# Ecrire les titres et sous-titres dans le fichier
ecrire_dans_fichier(nom_fichier, titres_sous_titres)

print("Les titres et sous-titres ont ete enregistres dans le fichier.")

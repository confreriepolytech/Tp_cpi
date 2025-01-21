import tkinter as tk
from tkinter import simpledialog

# Fonction pour récupérer les titres et sous-titres
def recuperer_titres():
    fenetre = tk.Tk()
    fenetre.withdraw()  # Masquer la fenêtre principale
    titres = simpledialog.askstring("Données", "Entrez les titres et sous-titres du cours :")
    return titres

# Ouvrir le fichier et écrire les titres
with open("Cahier_de_texte.txt", "a") as fichier:
    titres = recuperer_titres()
    fichier.write(titres + "\n")



import tkinter as tk
from tkinter import simpledialog

def recuperer_titres():
    root = tk.Tk()
    root.withdraw()  # Cacher la fenêtre principale
    with open("Cahier_de_texte.txt", "a") as fichier:
        while True:
            titre = simpledialog.askstring("Titre", "Entrez un titre ou sous-titre du cours (ou tapez 'fin' pour arrêter) :")
            if titre.lower() == 'fin':
                break  # Sortir de la boucle si l'utilisateur tape 'fin'
            fichier.write(f"Titre: {titre}\n")

# Appel de la fonction
recuperer_titres()


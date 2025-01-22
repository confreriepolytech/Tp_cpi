import tkinter as tk
from tkinter import simpledialog, messagebox

# Création du fichier "Cahier de texte"
filename = "Cahier de texte.txt"
f= open(filename, "a")
#Fonction principale pour saisir et enregistrer les titres/sous-titres
def ajouter_titres():
    # Création d'une fenêtre principale (nécessaire pour utiliser tkinter)
    root = tk.Tk()
    root.withdraw()  # Cache la fenêtre principale

    # Demande de titre
    titre = simpledialog.askstring("Saisie du titre", "Entrez le titre principal :")
    if not titre:
        messagebox.showinfo("Information", "Aucun titre principal saisi. Opération annulée.")
        return

    # Demande de sous-titres
    sous_titres = []
    while True:
        sous_titre = simpledialog.askstring("Saisie d'un sous-titre", "Entrez un sous-titre (ou laissez vide pour terminer) :")
        if not sous_titre:  # Sortir de la boucle si l'utilisateur laisse vide
            break
        sous_titres.append(sous_titre)

    #Enregistrement des données dans le fichier
    try:
        with open(filename, "a") as file:
            file.write(f"Titre : {titre}\n")
            for i, j in enumerate(sous_titres, start=1):
                file.write(f"  Sous-titre {i} : {j}\n")
            file.write("\n")  # Ajoute une ligne vide pour la lisibilité
        messagebox.showinfo("Succès", f"Le titre et les sous-titres ont été ajoutés à {filename}.")
    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible d'écrire dans le fichier : {e}")

#Lancer le processus
if __name__ == "__main__":
    ajouter_titres()

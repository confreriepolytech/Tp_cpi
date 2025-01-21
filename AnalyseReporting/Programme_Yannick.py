import PyPDF2
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

def lire_fichier(nom_fichier):
    try:
           with open(nom_fichier, 'rb') as fichier:
               lecteur = PyPDF2.PdfReader(fichier)
               contenu = ""
               for page in lecteur.pages:
                   contenu += page.extract_text()
               return contenu
    except FileNotFoundError:
           print(f"Le fichier {nom_fichier} est introuvable.")
           return ""

def recuperer_titres(contenu):
    titres = []
    for ligne in contenu:
        if ligne.startswith("Titre:") or ligne.startswith("Sous-titre:"):
            titres.append(ligne.strip())
    return titres

def afficher_boite_message(titres):
    if not titres:
        messagebox.showinfo("Information", "Aucun titre ou sous-titre trouvé.")
    else:
        for titre in titres:
            simpledialog.askstring("Titre/Sous-titre", f"Veuillez saisir les informations pour : {titre}")

def main():
    nom_fichier = "Cahier de texte.txt"
    contenu = lire_fichier(nom_fichier)
    titres = recuperer_titres(contenu)
    root = tk.Tk()
    root.withdraw()  # Masquer la fenêtre principale
    afficher_boite_message(titres)



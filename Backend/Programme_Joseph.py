# Importation des modules nécessaires
import tkinter as tk          
from tkinter import messagebox  

# Fonction pour ajouter un sous-titre
def ajouter_sous_titre():
    # Récupère le texte saisi dans le champ sous-titre
    sous_titre = sous_titre_entry.get()
    
    # Vérifie si un sous-titre a été saisi
    if sous_titre:
        # Ouvre le fichier en mode ajout ('a' pour append)
        with open("Cahier de texte.txt", "a") as fichier:
            # Écrit le sous-titre avec un tiret et un retour à la ligne
            fichier.write(f"    - {sous_titre}\n")
        
        # Efface le contenu du champ de saisie
        sous_titre_entry.delete(0, tk.END)
        
        # Affiche un message de confirmation
        messagebox.showinfo("Succès", "Sous-titre ajouté")

# Fonction pour ajouter un nouveau titre
def nouveau_titre():
    # Récupère le texte saisi dans le champ titre
    titre = titre_entry.get()
    
    # Vérifie si un titre a été saisi
    if titre:
        # Ouvre le fichier en mode ajout
        with open("Cahier de texte.txt", "a") as fichier:
            # Écrit le titre avec un saut de ligne avant
            fichier.write(f"\nTITRE: {titre}\n")
        
        # Efface le contenu du champ de saisie
        titre_entry.delete(0, tk.END)
        
        # Affiche un message de confirmation
        messagebox.showinfo("Succès", "Titre ajouté")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Cahier de texte")        # Définit le titre de la fenêtre
fenetre.geometry("300x200")             # Définit la taille de la fenêtre

# Section pour le titre
tk.Label(fenetre, text="Titre du cours:").pack()    # Étiquette pour le champ titre
titre_entry = tk.Entry(fenetre)                     # Champ de saisie pour le titre
titre_entry.pack()
tk.Button(fenetre, text="Nouveau titre",            # Bouton pour ajouter un titre
          command=nouveau_titre).pack()

# Section pour le sous-titre
tk.Label(fenetre, text="Sous-titre:").pack()        # Étiquette pour le champ sous-titre
sous_titre_entry = tk.Entry(fenetre)                # Champ de saisie pour le sous-titre
sous_titre_entry.pack()
tk.Button(fenetre, text="Ajouter sous-titre",       # Bouton pour ajouter un sous-titre
          command=ajouter_sous_titre).pack()

# Lancement de la boucle principale
fenetre.mainloop()    # Maintient la fenêtre ouverte 
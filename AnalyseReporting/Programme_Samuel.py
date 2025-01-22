import os
from tkinter import Tk, simpledialog, messagebox


def ajouter_titres_sous_titres():
    # Nom du fichier
    fichier_nom = "Cahier_de_texte.txt"

    # Vérifier si le fichier existe, sinon le créer
    if not os.path.exists(fichier_nom):
        with open(fichier_nom, "w") as fichier:
            fichier.write("=== Cahier de Texte ===\n\n")
        print(f"Fichier '{fichier_nom}' créé.")

    # Initialiser Tkinter (sans afficher la fenêtre principale)
    root = Tk()
    root.withdraw()  # Cache la fenêtre principale

    # Saisie des titres et sous-titres via des boîtes de dialogue
    titre = simpledialog.askstring("Saisie de Titre", "Entrez le titre du cours :")
    if titre is None:
        messagebox.showinfo("Information", "Aucune saisie pour le titre. Fin du programme.")
        return

    sous_titre = simpledialog.askstring("Saisie de Sous-titre", "Entrez le sous-titre du cours :")
    if sous_titre is None:
        messagebox.showinfo("Information", "Aucune saisie pour le sous-titre. Fin du programme.")
        return

    # Écriture des titres et sous-titres dans le fichier
    with open(fichier_nom, "a") as fichier:
        fichier.write(f"Titre : {titre}\n")
        fichier.write(f"Sous-titre : {sous_titre}\n\n")

    # Confirmation à l'utilisateur
    messagebox.showinfo("Succès", f"Les informations ont été ajoutées au fichier '{fichier_nom}'.")


# Appeler la fonction principale
if __name__ == "__main__":
    ajouter_titres_sous_titres()

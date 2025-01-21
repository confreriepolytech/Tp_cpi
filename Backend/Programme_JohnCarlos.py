import tkinter as tk
from tkinter import simpledialog, messagebox

# Nom du fichier
file_name = "Cahier_de_texte.txt"


def main():
    # Initialisation de l'interface tkinter
    root = tk.Tk()
    root.withdraw()  # Masquer la fenêtre principale

    try:
        # Charger ou créer le fichier
        with open(file_name, "a+") as file:
            file.seek(0)
            existing_content = file.read()

            if existing_content:
                messagebox.showinfo("Contenu existant", f"Voici le contenu actuel du fichier :\n\n{existing_content}")
            else:
                messagebox.showinfo("Information",
                                    "Le fichier est vide. Vous pouvez ajouter des titres et sous-titres.")

            # Saisir les titres et sous-titres
            titles = simpledialog.askstring("Saisie des titres", "Entrez les titres du cours :")
            subtitles = simpledialog.askstring("Saisie des sous-titres", "Entrez les sous-titres du cours :")

            # Vérifier les entrées et écrire dans le fichier
            if titles or subtitles:
                file.write(f"\n---\nTitre : {titles}\nSous-titres : {subtitles}\n")
                messagebox.showinfo("Succès", "Les informations ont été ajoutées au fichier.")
            else:
                messagebox.showwarning("Aucune entrée", "Aucun titre ou sous-titre saisi.")

    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")


if __name__ == "__main__":
    main()

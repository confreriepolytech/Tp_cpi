import tkinter as tk
from tkinter import simpledialog, messagebox
import os

# Chemin vers le fichier "Cahier de texte"
file_name = "Cahier_de_texte.txt"

def add_course_titles():
    # Vérifier si le fichier existe, sinon le créer
    if not os.path.exists(file_name):
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write("Cahier de Texte\n")
            file.write("=" * 20 + "\n\n")

    # Initialiser Tkinter
    root = tk.Tk()
    root.withdraw()  # Masquer la fenêtre principale

    # Demander le titre principal
    title = simpledialog.askstring("Titre", "Entrez le titre du cours :")
    if not title:
        messagebox.showinfo("Annulé", "Aucun titre n'a été ajouté.")
        return

    # Demander les sous-titres dans une boucle
    subtitles = []
    while True:
        subtitle = simpledialog.askstring("Sous-titre", "Entrez un sous-titre (ou laissez vide pour terminer) :")
        if not subtitle:  # Arrêter si l'utilisateur ne saisit rien
            break
        subtitles.append(subtitle)

    # Écrire les titres et sous-titres dans le fichier
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f"Titre : {title}\n")
        for i, subtitle in enumerate(subtitles, start=1):
            file.write(f"  {i}. {subtitle}\n")
        file.write("\n")

    messagebox.showinfo("Succès", f"Le titre et les sous-titres ont été ajoutés à {file_name}.")

# Appeler la fonction
if __name__ == "__main__":
    add_course_titles()

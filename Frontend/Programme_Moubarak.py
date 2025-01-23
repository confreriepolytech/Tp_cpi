import tkinter as tk
from tkinter import simpledialog

#code pour recuperer les titres
Titres_et_sous = simpledialog.askstring("Cahier de text.txt", "Entrez le titre à enregistrer:")

#definition d'une fonction pour saisir les titres
def saisir_titre(fichier_txt, content):
    with open(fichier_txt, 'a') as file:
        file.write(content + '\n')
        file.close()


# interface graphique pour la boite
root = tk.Tk()
root.withdraw()  # Masquer la fenêtre principale

saisir_titre("Cahier de text.txt", Titres_et_sous)

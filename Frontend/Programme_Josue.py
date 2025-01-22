import tkinter as tk
from tkinter import messagebox
from datetime import datetime


class CahierDeTexte:
    def __init__(self, root):
        self.root = root
        self.root.title("Cahier de Texte")
        self.root.geometry("500x400")

        # Création des variables
        self.titre_var = tk.StringVar()
        self.sous_titre_var = tk.StringVar()

        # Création des widgets
        self.creer_widgets()

    def creer_widgets(self):
        # Frame principale
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(expand=True, fill='both')

        # Label et Entry pour le titre
        tk.Label(main_frame, text="Titre du cours :", font=('Arial', 12)).pack(pady=5)
        titre_entry = tk.Entry(main_frame, textvariable=self.titre_var, width=50)
        titre_entry.pack(pady=5)

        # Label et Entry pour le sous-titre
        tk.Label(main_frame, text="Sous-titre :", font=('Arial', 12)).pack(pady=5)
        sous_titre_entry = tk.Entry(main_frame, textvariable=self.sous_titre_var, width=50)
        sous_titre_entry.pack(pady=5)

        # Boutons
        tk.Button(main_frame, text="Enregistrer", command=self.sauvegarder,
                  bg='#4CAF50', fg='white', font=('Arial', 12)).pack(pady=20)
        tk.Button(main_frame, text="Quitter", command=self.root.quit,
                  bg='#f44336', fg='white', font=('Arial', 12)).pack(pady=5)

    def sauvegarder(self):
        titre = self.titre_var.get().strip()
        sous_titre = self.sous_titre_var.get().strip()

        if not titre:
            messagebox.showerror("Erreur", "Veuillez saisir au moins un titre")
            return

        # Création du nom de fichier avec la date
        date = datetime.now().strftime("%Y-%m-%d")
        filename = f"Cahier_de_texte.txt"

        # Écriture dans le fichier
        try:
            with open(filename, 'a', encoding='utf-8') as f:
                f.write(f"\n{'='*50}\n")
                f.write(f"Date : {date}\n")
                f.write(f"Titre : {titre}\n")
                if sous_titre:
                    f.write(f"Sous-titre : {sous_titre}\n")
                f.write(f"{'='*50}\n")

            messagebox.showinfo("Succès", "Les informations ont été enregistrées avec succès!")

            # Réinitialisation des champs
            self.titre_var.set("")
            self.sous_titre_var.set("")

        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur est survenue : {str(e)}")

def main():
    root = tk.Tk()
    app = CahierDeTexte(root)
    root.mainloop()

if __name__ == "__main__":
    main()
import tkinter as tk
from tkinter import filedialog, messagebox
from docx import Document


def extract_titles_from_word():
    # Demander à l'utilisateur de sélectionner un fichier Word
    file_path = filedialog.askopenfilename(
        title="Sélectionnez un fichier Word",
        filetypes=[("Documents Word", "*.docx")]
    )
    
    if not file_path:
        return  # Si aucun fichier n'est sélectionné, sortir de la fonction

    try:
        # Charger le document Word
        doc = Document(file_path)

        # Listes pour stocker les titres par niveau
        titles = {1: [], 2: [], 3: []}  # Titres de niveau 1, 2 et 3

        # Parcourir tous les paragraphes du document
        for paragraph in doc.paragraphs:
            style_name = paragraph.style.name

            # Vérifier si le paragraphe est un titre
            if style_name == "Heading 1":  # Titre 1
                titles[1].append(paragraph.text.strip())
            elif style_name == "Heading 2":  # Titre 2
                titles[2].append(paragraph.text.strip())
            elif style_name == "Heading 3":  # Titre 3
                titles[3].append(paragraph.text.strip())

        # Préparer les résultats
        result = "Titres extraits :\n\n"
        for level, level_titles in titles.items():
            if level_titles:
                result += f"Titre {level} :\n"
                for title in level_titles:
                    result += f"  - {title}\n"

        # Afficher les résultats dans une boîte de message
        if any(titles.values()):
            messagebox.showinfo("Résultats", result)
        else:
            messagebox.showinfo("Résultats", "Aucun titre trouvé dans le document.")

    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")


# Interface utilisateur avec Tkinter
root = tk.Tk()
root.title("Extraction des Titres Word")
root.geometry("400x200")

# Bouton pour extraire les titres
btn = tk.Button(root, text="Extraire Titres depuis Word", command=extract_titles_from_word)
btn.pack(pady=20)

# Lancer la boucle principale Tkinter
root.mainloop()

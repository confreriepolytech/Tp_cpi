fichier_nom = "Cahier_de_texte.txt"

# Ouverture  lecture du fichier
f = open(fichier_nom, 'r', encoding='utf-8')
titres = f.readlines()
f.close()

# Affich des titres et sous-titres
print("Voici les titres et sous-titres récupérés :\n")
for ligne in titres:
    print(ligne.strip())


    
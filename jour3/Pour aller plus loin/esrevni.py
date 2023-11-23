def inverser_chaine(chaine):
    return chaine[::-1]

chaine_endroit = input("Entre un mot : ")
chaine_envers = inverser_chaine(chaine_endroit)

print("Chaine originale :", chaine_endroit)
print("Chaine inversée  :", chaine_envers)
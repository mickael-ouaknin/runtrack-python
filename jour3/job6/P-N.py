nombre = float(input("choisit un nombre : "))

def nombre_positif_negatif(nombre):
    if nombre > 0:
        return "positif"
    elif nombre < 0:
        return "negatif"
    else:
        return "nul"

resultat = nombre_positif_negatif(nombre)
print("Le nombre est", resultat)
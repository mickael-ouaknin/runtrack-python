def valeurpaires(liste):
    sommepaires = 0

    for nombre in liste:
        if nombre % 2 == 0:
            sommepaires += nombre

    return sommepaires


num = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
resultat = valeurpaires(num)

print(f"La somme des nombres pairs dans la liste est : {resultat}")

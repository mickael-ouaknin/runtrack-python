def pairimpair(nombre):
    if nombre < 0:
        raise ValueError("Le nombre doit être positif.")


    if nombre % 2 == 0:
        return True
    else:
        return False


nombre = float(input("Entre un nombre : "))


resultat = pairimpair(nombre)
print(resultat)
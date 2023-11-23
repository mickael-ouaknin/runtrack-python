def multiples(liste):
    count = 0

    for nbr in liste:
        if nbr % 3 == 0:
            count += 1

    return count


L = [8, 24, 48, 2, 16]
resultat = multiples(L)

print(f"Le nombre de multiples de 3 dans la liste est : {resultat}")
def afficher_tapis_diagonale(n):
    for i in range(n + 1):
        for j in range(n + 1):
            if i == j:
                print(' ', end='')
            else:
                print('#', end='')
        print()

taille_tapis = 10
afficher_tapis_diagonale(taille_tapis)
def tri_bulles(arr):
    n = 0
    for _ in arr:
        n += 1

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def arrondir_et_trier_liste(liste):
    n = 0
    for _ in liste:
        n += 1

    for i in range(n):
        entier = int(liste[i])
        decimale = liste[i] - entier
        if decimale >= 0.5:
            liste[i] = entier + 1
        else:
            liste[i] = entier
    tri_bulles(liste)


ma_liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
arrondir_et_trier_liste(ma_liste)
print("Liste arrondie et triée :", ma_liste)
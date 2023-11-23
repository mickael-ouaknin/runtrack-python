L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
somme = 1
for num in L:
    if (num > 25) and (num < 90):
        somme *= num

print(somme)
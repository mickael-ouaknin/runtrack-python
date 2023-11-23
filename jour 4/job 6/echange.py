def list():
    nbr = [1, 2, 3, 4, 5]
    print(nbr)
    a = nbr[0]
    nbr[0] = nbr[4]
    nbr[4] = a
    print(nbr)


nombre = list()
print(list)
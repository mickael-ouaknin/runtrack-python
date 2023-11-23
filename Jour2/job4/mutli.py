n = int(input("Entrez un entier supérieur à zéro (N) : "))
if n >= 1:
    for j in range (1,n+1) :
        print("Table de multiplication de : ",n)
        for i in range(1,11):
            print(i , " x ", j, " = ",i*j)

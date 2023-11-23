nom_produit = "Ordinateur portable"
prix_unitaire = 1000.0
quantite_stock = 50

print("Informations du produit:")
print("Nom:", nom_produit)
print("Prix unitaire:", prix_unitaire)
print("Quantité en stock:", quantite_stock)

ajout_quantite = int(input("Encore 200 exemplaires "))
quantite_stock += ajout_quantite

prix_unitaire *= 1.1

print("\nInformations mises à jour du produit:")
print("Nom:", nom_produit)
print("Prix unitaire (après augmentation de 10%):", prix_unitaire)
print("Quantité en stock (après ajout):", quantite_stock)

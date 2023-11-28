def distance_totale_semaine(marches, hauteur_marche_cm):
    hauteur_marche_m = hauteur_marche_cm / 100
    distance_par_aller_retour = marches * hauteur_marche_m * 2
    distance_par_jour = distance_par_aller_retour * 5
    distance_par_semaine = distance_par_jour * 7

    return distance_par_semaine

nombre_marches = int(input("Entrez le nombre de marches du phare : "))
hauteur_marche = float(input("Entrez la hauteur de chaque marche en cm : "))

distance = distance_totale_semaine(nombre_marches, hauteur_marche)
print(f"\nPour {nombre_marches} marches de {hauteur_marche} cm, le gardien parcourt {distance:.2f} m par semaine.")

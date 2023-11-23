def time_to_text(minutes):
    heures = minutes // 60
    minutes = minutes % 60
    texte = str(heures) + " heures et " + str(minutes) + " minutes"
    return texte

minutes = int(input("Entre un entier en minute : "))

resultat = time_to_text(minutes)
print(resultat)
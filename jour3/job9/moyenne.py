def moyenne():
    note1 = float(input("Entrez la première note : "))
    note2 = float(input("Entrez la deuxième note : "))
    note3 = float(input("Entrez la troisième note : "))
    
    moyenne_etudiant = (note1 + note2 + note3) / 3
    
    if 15 <= moyenne_etudiant <= 20:
        return "Très bon élève"
    elif 11 <= moyenne_etudiant <= 14:
        return "Bon élève"
    elif 8 <= moyenne_etudiant <= 10:
        return "Assez moyen"
    elif 0 <= moyenne_etudiant <= 7:
        return "Élève devant faire des efforts"
    else:
        return "Note invalide"

resultat = moyenne()
print(resultat)
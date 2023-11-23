montant_initial = 10000 
taux_rendement_annuel = 5 

def calculer_gain_annuel(montant, taux):
    gain = montant * (taux / 100)
    return gain

gain_initial = calculer_gain_annuel(montant_initial, taux_rendement_annuel)
print(f"Le gain annuel initial est de {gain_initial} euros.")

montant_initial += 5000
taux_rendement_annuel += 2

nouveau_gain = calculer_gain_annuel(montant_initial, taux_rendement_annuel)
print(f"\nAprès l'augmentation du capital et du taux, le nouveau gain annuel est de {nouveau_gain} euros.")

montant_initial -= montant_initial * 0.1
taux_rendement_annuel -= 1

montant_final = montant_initial + calculer_gain_annuel(montant_initial, taux_rendement_annuel)
print(f"\nAprès le retrait et la diminution du rendement, le montant final de l'investissement est de {montant_final} euros.")

Apple_60 = 20 * 60
Apple_145 = 10* 145
Prix_action_actuel = 135

# Question 1
Apple_revente = 8 * 120
Compte_titre = Apple_60 + Apple_145 - Apple_revente # Il lui reste donc 30 - 8 = 22 actions Apple 
print('Le montant des actions actuelles présentes sur le compte titre de John est de :', Compte_titre, '$')

# Question 2
Prix_moyen_achat = Apple_60 + Apple_145 / 30
print('Le Prix d\'achat moyen des action est de :', Prix_moyen_achat , '$')

# Question 3
Totale_action = 22 * Prix_action_actuel
Plus_value_totale = Totale_action - Compte_titre
print('la plues-value totale est de :', Plus_value_totale,'$')

# Question 4
Calcul_plus_value_France = Plus_value_totale * 30 / 100
print('En déclarant votre Plus-value en France vous devriez payer 30% de taxe soit :', Calcul_plus_value_France, '$')


Calcul_plus_value_Belgique = (Plus_value_totale - 500) * 40 / 100
print('En déclarant votre Plus-value en Belgique vous devriez payer, après déduction des 500 $ d\'abattements :', Calcul_plus_value_Belgique, '$')

if Calcul_plus_value_France > Calcul_plus_value_Belgique :
    print('Il est plus intéressant de déclarer votre Plus-value en Belgique')

else :
    print('il est plus intéressant de déclarer votre Plus-value en France')



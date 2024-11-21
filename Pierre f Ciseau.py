import random

options['pierre', 'feuille' ,'ciseaux']
score_joueur = 0
score_ordi = 0
manche = 5

print("bienvenue dans ce jeu de pierre feuille ciseau")
print(f"le jeu se joue en {manche} manches bonne chance")

for manche in range (manche) :
    choix_ordi = random.choices(options)
    choix_joueur = input("choisi entre 'pierre' 'feuille' 'ciseaux' : ").lower()

    if choix_joueur not in options :
        print("écris bien tête de nouille ! ")

    if choix_joueur == choix_ordi :
        print("égalité")
    elif (choix_joueur == "pierre" and choix_ordi == ciseaux) or\
        (choix_joueur == "feuille" and choix_ordi == pierre) or\
        (choix_joueur == "ciseaux" and choix_ordi == feuille) :
        print("tu gange cette manche avec un score de")
    score_joueur += 1
    else:
        print(f"l'ordi gagne cette manche avec un score de {score_joueur} pour toi à {score_ordi} ")
    score_ordi += 1


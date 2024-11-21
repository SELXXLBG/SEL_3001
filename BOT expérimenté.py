from random import randint
import random

name_du_bot = "pablo"
name = (input("c'est quoi ton nom ? ")).lower()
print(f"salut {name} moi c'est {name_du_bot} !")
print("je vais te poser des questions et te faire jouer à des jeux t'es prêt ? ")

age = int(input("t'as quel age ? "))
age_du_bot = 28
if age<age_du_bot:
    print(f"tu es plus jeune que moi, j'ai {age_du_bot} ans ")
elif age>age_du_bot:
    print(f"t'es plus vieux que moi, j'ai {age_du_bot} ans ")
else:
    print("on a le même age !!")

couleur = (input("quelle est ta couleur préférée ? "))
bot_color = "bleu"
if couleur == bot_color:
    print("incroyable j'adore cette couleur aussi !")
else:
    print(f"le {couleur} est une très belle couleur")

petite_question = input("24 fois 486 ça fait combien ? ")
if petite_question == "11664" :
    print("t'es chaud GG!")
else:
    print("bahahaha trop nul")


tentatives = 0
limit_essais = 5
nbm_aléatoire = randint(1,20)
while tentatives < limit_essais:
    tentatives +=1
    nbm_aleatoire_user = int(input("donne un nombre de 1 à 20 : "))
    if nbm_aleatoire_user<nbm_aléatoire:
        print(f"un chiffre plus grand que {nbm_aleatoire_user}")
    elif nbm_aleatoire_user>nbm_aléatoire:
        print(f"un chiffre plus petit que {nbm_aleatoire_user}")
    else:
        print("bravo t'es le goat")
        break
if limit_essais == tentatives and nbm_aléatoire != nbm_aleatoire_user :
    print(f" PERDU ! Tu as épuisé toute tes chances ! le chiffre à trouver était {nbm_aléatoire} ")

print("maitenant tu vas jouer à pierre feuille ciseaux contre moi c'est partit ! ")

options = [ "pierre" , "feuille" , "ciseaux" ]
score_joueur = 0
score_ordinateur = 0
manches = 5

for manche in range (manches) :
    choix_ordi = random.choice(options)
    choix_joueur = input("choisi entre 'pierre' 'feuille' et 'ciseaux' : ").lower()

    if choix_joueur not in options :
        print("écris bien tête de neuille")

    print(f"{name_du_bot} à choisi {choix_ordi}")

    if choix_ordi == choix_joueur :
        print("égalité !")
    elif (choix_joueur == 'pierre' and choix_ordi == 'ciseaux') or \
         (choix_joueur == 'ciseaux' and choix_ordi == 'feuille') or \
         (choix_joueur == 'feuille' and choix_ordi == ' pierre') :
         print("tu remporte cette manche !")
         score_joueur += 1
    else :
        print(f"{name_du_bot} gagne cette manche !")
        score_ordinateur +=1

    print(f"{name_du_bot} a {score_ordinateur} et {name} a {score_joueur} ! ")

print("partie terminée")
if score_joueur > score_ordinateur :
    print(f"{name} gagne cette partie avec un score de {score_joueur} a {score_ordinateur} ! ")
elif score_joueur < score_ordinateur :
    print (f"t'as perdu {name_du_bot} à {score_ordinateur} et toi t'as {score_joueur} ! ")
else :
    print ("égalité !")


print("maintenant, on vas jouer à pile ou face(t'as pas le choix)")
Pile_Faces_choix = [ "pile" , "face"]
score_player = 0
score_PC = 0
manchees = 5

for manchees in range (manchees) :
    choix_PC = random.choice(Pile_Faces_choix)  
    choix_player = input(" choisi entre Pile ou Face : ") 

    if choix_player not in Pile_Faces_choix :
        print("écris bien tete de neuille ! ") 
    print(f"{name_du_bot} à choisi {choix_PC} ")

    if choix_PC == choix_player :
        print(f"Egalité, le score reste à {score_player} pour toi et {score_PC} pour {name_du_bot} ")
    elif (choix_player == "face" and choix_PC == "pile") :
        print(f"tu gagne cette manche avec un score de {score_player} pour toi à {score_PC} ! ")
    score_player += 1
    else:
        print(f"{name_du_bot} gagne avec un score de {score_PC} pour lui à {score_player} pour toi ")
    score_PC += 1
    

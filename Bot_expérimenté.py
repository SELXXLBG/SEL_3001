import random
name = (input("c'est quoi ton nom ? ")).lower()
name_bot = ("Pedro")
if name == "selyan" :
    print ("ce nom est juste le meilleur")
else :
    print(f"{name} est un très beau nom moi c'est {name_bot}")

print("je vais te poser des questions et te faire jouer a qlq jeux c'est partit !")

coffee = input("tu veux un café ? ").lower
if coffee = "oui" :
    print("bas lève toi de ton lit gros flemmard t'as cru j'étais ton esclave ? ")
else :
    print("bois de l'eau comme même c'est meilleur pour la santé ")

limite_essais = 5
tentatives = 0
nombre_aleatoire = random.randint(1,20)

while tentatives < limite_essais :
    tentatives += 1
    nmb_user = int(input("choisis un nombre de 1 à 20 : "))
    if nombre_aleatoire > nmb_user :
         print(f"un nombre plus grand que {nmb_user}")
    elif nombre_aleatoire < nmb_user :
        print(f"un nombre plus petit que {nmb_user}")
    else :
        print("bravo t'es le goat")
        break

if tentatives == limite_essais and nombre_aleatoire != nmb_user :
    print(f"t'as épuisé toute tes chances  le nombre à trouvé était {nombre_aleatoire} ! ")



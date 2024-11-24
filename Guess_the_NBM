import random
nbm_random = random.randint(1,10)
essais = 0
essais_max = 5

print("tu vas jouer a 'Guess the numbers' t'as 5 essais bonne chance ! ")
while essais < essais_max :
    reponds = int(input("choisi un nombre entre 1 et 10 : "))
    if reponds > nbm_random :
        print(f"choisi un nombre plus petit que {reponds}")
        essais += 1
        print(f"il te reste {essais_max - essais} essais ")
    elif reponds < nbm_random :
        print(f"choisi un nombre plus grand que {reponds}")
        essais += 1
        print(f"il te reste {essais} essais ")
    else : 
        print(F"Bravo !! le nombre à trouvé été belle et bien {nbm_random} ! ")
        break
    if essais >= essais_max :
        print(f"t'as perdu le nombre à trouver était {nbm_random}")
        break

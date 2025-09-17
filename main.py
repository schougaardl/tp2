"""
petit jeux de divinette
par Lars Schougaard 406
"""
import random

while True:
    nb = random.randint(1, 10)
    nb_essai = 0
    print("J'ai choisi un nombre au hasard entre 0 et 10. A vous de le deviner.")
    essai = int(input("Entre votre essai: "))

    while True:

        nb_essai += 1

        if  nb < essai:
            print(f"mauvais choix le nombre est plus petit que {essai}.")

        if  nb > essai:
            print(f"mauvais choix le nombre est plus grand que {essai}.")

        if essai == nb:
            break

        essai = int(input("Entre votre essai: "))

    print(f"Bravo! Bonne reponse. Vous avez réusi en : {nb_essai} essai.")
    rejouer = input("Voulez vous rejouer,oui ou non?")

    if rejouer == "non":
        break


print("Merci et aurevoire")

"""
petit jeux de divinette
par Lars Schougaard 406
"""
import random


def bornes():
    mini = int(input("que vouler vous que le nombre le plus petit soit :"))
    maxi = int(input("que vouler vous que le nombre le plus grand soit soit :"))
    return mini, maxi


while True:
    minimum, maximum = bornes()
    nb = random.randint(minimum, maximum)
    nb_essai = 0
    print(f"J'ai choisi un nombre au hasard entre {minimum} et {maximum}. A vous de le deviner.")
    essai = int(input("Entre votre essai: "))

    while True:
        essai = int(input("Entre votre essai: "))

        nb_essai += 1

        if nb < essai:
            print(f"mauvais choix le nombre est plus petit que {essai}.")

        if nb > essai:
            print(f"mauvais choix le nombre est plus grand que {essai}.")

        if essai == nb:
            break

    print(f"Bravo! Bonne reponse. Vous avez réusi en : {nb_essai} essai.")
    rejouer = input("Voulez vous rejouer,oui ou non?")

    if rejouer == "non":
        break


print("Merci et aurevoire")

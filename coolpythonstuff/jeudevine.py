import random
count=0
nb=-1
x=random.randint(0,100)
print("Bienvenu ce jeu consiste à deviner un nombre vous avez droit à 6 essaies ")
while nb!=x:
    if count==6:
        print("Perdu")
        print("le nombre est ",x)
        break
    nb=int(input("Entrer un nombre compris entre 0 et 100 : "))
    if nb<x:
        print("le nombre mystérieux est plus grand que le votre")
        count+=1
    elif nb>x:
        print("le nombre mystérieux est plus petit que le votre")
        count+=1
    else:
        print("Gagné felicitation!!!!")


import random


def jeu():
    print("Bienvenue Dans votre jeu de devinette de nombre (Vous avez 6 essais (! )\n\n          Bonne Chance ...\n\n")
    x=random.randint(100,999)
    #print(x)
    #nb=int(899.9*random.random()+100
    count=0
    nb=000
    essai=0
    while nb!=x and essai!=6:
        gd=0
        nb=input("Entrer un nombre de 3 chiffres : ")
        while len(nb)!=3 or nb.isdigit()==False:
            nb=input("erreur,  Entrer un nombre de 3 chiffre !!! : ")
        essai+=1
        count+=1
        x=str(x)
        for i in range (0,3):
            if nb[i]==x[i]:
                gd+=1
        if gd==0:    
            print("pas de chiffre de Bon")
        elif gd==1:
            print("1 chiffre de Bon")
        elif gd==2:
             print("2 chiffres de Bon")
    if gd==3:
        print("gagné, Félicitation.. (:")
    if essai==6:
        print("Perdu ):")


jeu()

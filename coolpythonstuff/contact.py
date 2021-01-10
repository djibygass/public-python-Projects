liste=["nom","prénom","mail","téléphone"];choix='d'

chemin="C:\\Users\\Administrateur\\AppData\\Local\\Programs\\Python\\Python38-32\\contact.txt"



print("Bienvenue sur votre Application de gestion de contact \n")
print("           Que Voulez-vous faire ?\n")
while choix!='6':
    choix=input("1- Afficher la liste de vos contacts\n\n2- Ajouter un nouveau contact\n\n3- Rechercher un contact\n\n4- Modifier un contact\n\n5- Supprimer un contact\n\n6-Quitter\n\n --> ")
    print("\n")
    while choix!='1' and choix!='2' and choix!='3' and choix!='4' and choix!='5' and choix!='6':
         choix=input("Erreur, \n\n1- Afficher la liste de vos contacts\n\n2- Ajouter un nouveau contact\n\n3- Rechercher un contact\n\n4- Modifier un contact\n\n5- Supprimer un contact\n\n6-Quitter\n\n --> ")
         print("\n")
         
#AFFICHAGE
    if choix=='1':
        f=open(chemin,"r")
        affiche=f.readlines()
        for i in affiche:
             liste=i.split()
             print(liste)
             print("\n")
        f.close()

#AJOUT    
    elif choix=='2':
        nb=0
        recom='o'
        nbr=0
        while recom=='o' or recom=='O':
            nbr+=1
            nom=input("Entrer le nom : ")
            while len(nom)==0:
                nom=input("Erreur, Entrer un nom svp : ")
            prenom=input("Entrer le prénom (separer par '_' si vous avez deux prenom svp : ")
            while len(prenom)==0:
                prenom=input("Erreur, Entrer un prenom svp : ")
            mail=input("Entrer l'adresse mail : ")
            while '@' not in mail or '.' not in mail :
                mail=input("Erreur, Entrer l'adresse mail : ")
            tel=input("Entrer le numéro de téléphone : ")
            while tel.isdigit()==False or len(tel)!=10:
                tel=input("Erreur, Entrer le numéro de téléphone : ")

            f=open(chemin,"r")
            affiche=f.readlines()
            for i in affiche:
                 liste=i.split()
                 for a in liste:
                     if a==tel or a==mail:
                         nb=1
            f.close()
            if nb==1:
                print("Désolé ce contact existe déja")
                nbr-=1
            elif nb==0:
                nom=nom.upper()
                liste=[nom,prenom,mail,tel]
                liste="    ".join(liste)
                f=open(chemin,"a")
                
                f.write(liste)
                f.write("\n")
                f.close()
            recom=input("Voulez-vous ajouter un autre contact ? si oui taper O ou o : ")
            print("\n")
            if recom!='o' and recom!='O':
                break
        if nbr==1:
            print("vous avez ajouté",nbr," seul Contact")
            print("\n")
        else:
            print("vous avez ajouté",nbr," Contacts")
            print("\n")

#RECHERCHE            
    elif choix=='3':
        print("Vous voulez faire une recherche, il faut au moins une information.\n soit un nom, un prénom, une adresse mail ou un numéro de téléphone.\n")
        parquoi=input("Entrer (n ou N)pour une recherche par nom\n(p ou P) par prénom\n(m ou M) par mail\n(t ou T) par numéro de téléphone\n -> ")
        print("\n")
        while parquoi!='n' and parquoi!='N' and parquoi!='p' and parquoi!='P' and parquoi!='m' and parquoi!='M' and parquoi!='t' and parquoi!='T':
            parquoi=input("Erreur, \nEntrer (n ou N)pour une recherche par nom\n(p ou P) par prénom\n(m ou M) par mail\n(t ou T) par numéro de téléphone\n -> ")
            print("\n")
        if parquoi=='n' or parquoi=='N':
            nb=0
            achercher=input("Entrer le nom : ")
            while len(achercher)==0:
                achercher=input("Erreur, Entrer un nom svp : ")
            achercher=achercher.upper()
            f=open(chemin,"r")
            affiche=f.readlines()
            for i in affiche:
                 liste=i.split()
                 for a in liste:
                     if a==achercher:
                         
                         #print(liste)
                         nb=1
                         print(" contact\nNom :     ",achercher,"\nPrénom :    ",liste[1],"\nMail :      ",liste[2],"\nTéléphone :    ",liste[3],"\n\n")
                         break           
            if nb==0:
                print("Désolé, ce contact ne figure pas dans votre répertoire")
                print("\n")

        elif parquoi=='p' or parquoi=='P':
            nb=0
            achercher=input("Entrer le prénom : ")
            while len(achercher)==0:
                 achercher=input("Erreur, Entrer un prénom svp : ")
            f=open(chemin,"r")
            affiche=f.readlines()
            for i in affiche:
                 liste=i.split()
                 for a in liste:
                     if a==achercher:
                         #print(liste)
                         nb=1
                         print(" contact\nNom :     ",liste[0],"\nPrénom :    ",achercher,"\nMail :      ",liste[2],"\nTéléphone :    ",liste[3],"\n\n")
                         break           
            if nb==0:
                print("Désolé, ce contact ne figure pas dans votre répertoire")
                print("\n")

                
            
        elif parquoi=='m' or parquoi=='M':
            nb=0
            achercher=input("Entrer le mail : ")
            while '@' not in achercher or '.' not in achercher :
                achercher=input("Erreur, Entrer une adresse mail : ")
            f=open(chemin,"r")
            affiche=f.readlines()
            for i in affiche:
                 liste=i.split()
                 for a in liste:
                     if a==achercher:
                         #print(liste)
                         nb=1
                         print(" contact\nNom :     ",liste[0],"\nPrénom :    ",liste[1],"\nMail :      ",achercher,"\nTéléphone :    ",liste[3],"\n\n")
                         break           
            if nb==0:
                print("Désolé, ce contact ne figure pas dans votre répertoire")
                print("\n")


        else:
            nb=0
            achercher=input("Entrer le numéro de teléphone : ")
            while achercher.isdigit==False or len(achercher)!=10:
                achercher=input("Erreur, Entrer un numéro de téléphone : ")
            f=open(chemin,"r")
            affiche=f.readlines()
            for i in affiche:
                 liste=i.split()
                 for a in liste:
                     if a==achercher:
                         nb=1
                         print(" contact\nNom :     ",liste[0],"\nPrénom :    ",liste[1],"\nMail :      ",liste[2],"\nTéléphone :    ",achercher,"\n\n")
                         break           
            if nb==0:
                print("Désolé, ce contact ne figure pas dans votre répertoire")
                print("\n")

#MODIFICATION
    elif choix=='4':
        nb=0
        amodif=input("Entrer une info sur contact à modifier (NOM, prenom, mail ou téléphone : ")
        while len(amodif)==0:
            amodif=input("Erreur, Entrer le nom du contact à modifier : ")
        f=open(chemin,"r")
        affiche=f.readlines()
        for i in affiche:
             liste=i.split()
             for a in liste:
                 if a==amodif:
                     liste="    ".join(liste)
                     id=affiche.index(liste+"\n")
                     liste=i.split()
                     nb=1
                     print(" contact\n1-Nom :     ",liste[0],"\n2-Prénom :    ",liste[1],"\n3-Mail :      ",liste[2],"\n4-Téléphone :    ",liste[3],"\n")
                     x=(input("Que voulez vous modifier ? --> "))
                     while x!='1' and  x!='2' and  x!='3' and  x!='4':
                         print(" contact\n1-Nom :     ",liste[0],"\n2-Prénom :    ",liste[1],"\n3-Mail :      ",liste[2],"\n4-Téléphone :    ",liste[3],"\n")
                         x=(input("Que voulez vous modifier ? --> "))
                     if x=='1':
                         remp=input("Entrer le nouveau nom : ")
                         while len(remp)==0:
                             remp=input("Erreur, Entrer le nouveau nom svp : ")
                         remp=remp.upper()
                         liste[0]=remp
                         liste="    ".join(liste)
                         liste=liste+"\n"
                         f=open(chemin,"w")
                         affiche[id]=liste
                         affiche="".join(affiche)
                         f.write(affiche)
                         f.close()
                         print("\n")
                     elif x=='2':
                         remp=input("Entrer le nouveau prénom : ")
                         while len(remp)==0:
                             remp=input("Erreur, Entrer le nouveau prénom svp : ")
                         liste[1]=remp
                         liste="    ".join(liste)
                         liste=liste+"\n"
                         f=open(chemin,"w")
                         affiche[id]=liste
                         affiche="".join(affiche)
                         f.write(affiche)
                         f.close()
                         print("\n")
                     elif x=='3':
                         remp=input("Entrer le nouveau mail : ")
                         while '@' not in remp or '.' not in remp :
                             remp=input("Erreur, Entrer l'adresse mail : ")
                         liste[2]=remp
                         liste="    ".join(liste)
                         liste=liste+"\n"
                         f=open(chemin,"w")
                         affiche[id]=liste
                         affiche="".join(affiche)
                         f.write(affiche)
                         f.close()
                         print("\n")
                     elif x=='4':
                         remp=input("Entrer le nouveau Numéro de téléphone : ")
                         while remp.isdigit()==False or len(remp)!=10:
                             remp=input("Erreur, Entrer le nouveau Numéro de téléphone : ")
                         liste[3]=remp
                         liste="    ".join(liste)
                         liste=liste+"\n"
                         f=open(chemin,"w")
                         affiche[id]=liste
                         affiche="".join(affiche)
                         f.write(affiche)
                         f.close()
                         print("\n")
                                              
        if nb==0:
             print("Désolé, ce contact ne figure pas dans votre répertoire")
             print("\n")
    
#SUPPRESSION        
    elif choix=='5':
        nb=0#testeur
        asupp=input("Entrer une info sur contact à supprimer (NOM, prenom, mail ou téléphone : ")
        while len(asupp)==0:
            asupp=input("Erreur, Entrer une info sur contact à supprimer  : ")
        f=open(chemin,"r")
        affiche=f.readlines()
        for i in affiche:
             liste=i.split()
             for a in liste:
                 if a==asupp:
                     liste="    ".join(liste)
                     id=affiche.index(liste+"\n")
                     liste=i.split()
                     nb=1#test
                     print(" contact\nNom :     ",liste[0],"\nPrénom :    ",liste[1],"\nMail :      ",liste[2],"\nTéléphone :    ",liste[3],"\n")
                     conf=input("Voulez-vous supprimer ce contact ? (o ou O) pour Oui\n ---> ")
                     if conf=='o' or conf=='O':
                         affiche.pop(id)
                         affiche="".join(affiche)
                         f=open(chemin,"w")
                         f.write(affiche)
                         f.close()
                         print("\n")
                     else:
                         print("\n")
        if nb==0:
            print("Désolé, ce contact ne figure pas dans votre répertoire")
            print("\n")


    else:
        print("Au revoir (:")











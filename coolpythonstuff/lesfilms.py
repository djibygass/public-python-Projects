listsmanga=["naruto","onepiece","hunterxhunter","myhero","erased","baki"];choix=1
while choix!=7:
    print("Bienvenu sur votre programme de gestion Manga (;\n\n           Que voulez-vous faire ?\n\n")
    choix=int(input("1-Afficher la liste de vos mangas\n\n2-Ajouter un titre à la liste\n\n3-Afficher le nombre de manga\n\n4-Supprimer un manga\n\n5-Modifier un titre\n\n6-Trier vos mangas\n\n7-Quitter\n\n --> "))

    while choix<1 or choix>7:
        choix=int(input("1-Afficher la liste de vos mangas\n\n2-Ajouter un titre à la liste\n\n3-Afficher le nombre de manga\n\n4-Supprimer un manga\n\n5-Modifier un titre\n\n6-Trier vos mangas\n\n7-Quitter\n\n --> "))   
    if choix==1:
        print(listsmanga)
    #elif choix==2:
    

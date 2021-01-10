choix=1
while choix!=4:
    print("BONJOUR BIENVENU SUR LE MENU")
    choix=int(input("FAITE VOTRE CHOIX\n\n1-Année Bissextile\n\n2-Equation du secon degré\n\n3-calculette\n\n4-quitter\n\n--> "))

    while choix<1 or choix>4:
        choix=int(input("ERREUR DE CHOIX\n\nVEUILLEZ RECOMMENCER\n\n1-Année Bissextile\n\n2-Equation du secon degré\n\n3-calculette\n\n4-quitter\n\n--> "))

    if choix==1:
        print("ANNEE BISSEXTILE\n\n")
    elif choix==2:
        print("EQUATION DU SECOND DEGRE\n\n")
    elif choix==3:
        print(" CALCULETTE + - * /\n\n")
    else:
        print("A BIENTOT\n\n")

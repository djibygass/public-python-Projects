
import mysql.connector
bdd=mysql.connector.connect(host="localhost",user="root",password="",database="hopital")
curseur=bdd.cursor()
#concaténation pour variable au cas où il faudra entrer le nom de la table (!


    


def access():
        
    def affiche():
        curseur.execute("select * from medecins")
        for toubib in curseur.fetchall():
            print(toubib)
        print("\n")
        menu()

        
    def ajout():
        m_nom=input("Entrer le nom du medecin : ")
        m_prenom=input("Entrer le prenom du medecin : ")
        m_specialite=input("Entrer la specialite du medecin : ")
        m_service=int(input("Entrer le service du medecin : "))
        m_service=str(m_service)
        st="'"+m_nom+"'"+","+"'"+ m_prenom+"'"+","+"'"+ m_specialite+"'"+","+"'"+ m_service+"'"
        curseur.execute("insert into medecins (nom,prenom,specialite,service) values ("+ st +")")
        print("c'est fait !")
        print("\n")
        menu()

        
    def modif():
        amodif=input("Entre le nom du medecin à modifier : ")
        curseur.execute("select * from medecins where nom ="+"'"+amodif+"'")
        count=0
        for toubib in curseur.fetchall():
            print(toubib)
            count+=1
        if count==0:
            print("Désolé ce nom ne figure pas dans la base de donnée de notre hopital")
            modif()
        if count>=1 :
            ID__=int(input("Entre le numéro du medecin que vous souhaitez modifier : "))
            ID__=str(ID__)
            choix=input("\n Tapez (1) pour modifier le nom \n Tapez (2) pour modifier le prenom \n Tapez (3) pour modifier le service et la spécialité \n Tapez (4) pour Tout modifier\n ---> ")
            if choix=='1':
                m_nom=input("Entrer le nouveau nom : ")
                st="'"+m_nom+"'"
                curseur.execute("Update medecins set medecins.nom ="+st+"where medecins.numed="+ID__)
                print("C'est fait !")
            elif choix=='2':
                m_prenom=input("Entrer le nouveau prenom : ")
                st="'"+m_prenom+"'"
                curseur.execute("update medecins set medecins.prenom ="+st+"where medecins.numed="+ID__)
                print("C'est fait !")
            elif choix=='3':
                curseur.execute("select numserv,nomserv from services")
                for bibtou in curseur.fetchall():
                    print(bibtou)
                m_service=int(input("Entrer le numéro de service : "))
                m_service=str(m_service)
                m_specialite=input("Entrer la nouvelle spécialité : ")
                st1="'"+m_service+"'"
                st2="'"+m_specialite+"'"
                curseur.execute("update medecins set medecins.service="+st1+"where medecins.numed="+ID__)
                curseur.execute("update medecins set medecins.specialite="+st2+"where medecins.numed="+ID__)
                print("C'est fait !")
            elif choix=='4':
                m_nom=input("Entrer le nouveau nom : ")
                m_prenom=input("Entrer le nouveau prénom : ")
                m_specialite=input("Entrer la nouvelle spécialite : ")
                m_service=input("Entrer le nouveau numéro de service : ")
                curseur.execute("update medecins set medecins.nom="+"'"+m_nom+"'"+"where medecins.numed="+ID__)
                curseur.execute("update medecins set medecins.prenom="+"'"+m_prenom+"'"+"where medecins.numed="+ID__)
                curseur.execute("update medecins set medecins.specialite="+"'"+m_specialite+"'"+"where medecins.numed="+ID__)
                curseur.execute("update medecins set medecins.service="+"'"+m_service+"'"+"where medecins.numed="+ID__)
                print("C'est fait !")
        print("\n")
        menu()

        
    def supp():
        count=0
        m_nom=input("Entrer le nom du medecin à supprimer : ")
        curseur.execute("Select * from medecins where medecins.nom="+"'"+m_nom+"'")
        for toubib in curseur.fetchall():
            print(toubib)
            count+=1
        if count==0:
            print("Il n'y a aucun medecin de ce nom dans notre base de donnée.")
        else:
            ID__=input("Entrer le numéro du medecin : ")
            curseur.execute("Delete from medecins where numed="+ID__)
            print("C'est fait !")    
        print("\n\n")
        menu()
        

    def recherche():
        print("Entrer le nom du medecin que vous rechercher svp")
        m_nom=input("--> ")
        curseur.execute("Select * from medecins where medecins.nom="+"'"+m_nom+"'")
        count=0
        for toubib in curseur.fetchall():
            print(toubib)
            count+=1
        if count==0:
            print("Il n'y a aucun medecin de ce nom dans notre base de donnée.")
            recherche()
        print("\n\n")
        menu()
        
        
            
            
        
        


    def menu():
        choix=input("\n1- Afficher les medecins\n\n2- Ajouter un medecin\n\n3- modifier un medecin\n\n4- Supprimer\n\n5- Rechercher un medecin\n\n6- quitter\n\n --->> ")
        while choix!='1' and choix!='2' and choix!='3' and choix!='4' and choix!='5' and choix!='6':
            choix=input("\n1- Afficher les medecins\n\n2- Ajouter un medecin\n\n3- modifier un medecin\n\n4- Supprimer\n\n5- Rechercher un medecin\n\n --->> ")
        if choix=='6':
            print("Ciao")
            exit
        elif choix=='1':
            affiche()
        elif choix=='2':
            ajout()
        elif choix=='3':
            modif()
        elif choix=='4':
            supp()
        else:
            recherche()
            
            
    menu()




def check(identifiant):
    count=0
    curseur.execute("select * from user where identifiant="+"'"+identifiant+"'")
    for usr in curseur.fetchall():
        count+=1
    if count==1:
        return True
    else:
        return False

def checkk(mdp):
    count=0
    curseur.execute("select * from user where mdp="+"'"+mdp+"'")
    for usr in curseur.fetchall():
        count+=1
    if count==1:
        return True
    else:
        return False



def connect():    
    ID=input("Entrer votre identifiant : ")
    #curseur.execute("select * from user where identifiant="+"'"ID"'")
    #for usr
    check(ID)
    if check(ID)==True:
        mdp_=input("Entrer votre mot de passe : ")
        checkk(mdp_)
        if checkk(mdp_)==True:
            access()
        else:
            print("Mot de passe incorrect !")
            connect()
    else:
        print("Identifiant non reconnu !")
        connect()
        
    
    
def subscribe():
    ID=input("Entrer votre identifiant : ")
    if check(ID)==True:
        print("Désolé cet identifiant existe déja..")
        subscribe()
    mdp_=input("Entrer votre mot de passe : ")
    mail_=input("Entrer votre adresse mail : ")
    while '@' not in mail_ or '.' not in mail_:
        mail_=input("mail non valide ! Entrer votre adresse mail : ")
    st="'"+ID+"'"+","+"'"+mdp_+"'"+","+"'"+mail_+"'"
    curseur.execute("insert into user (identifiant,mdp,mail) values ("+st+")")
    print("C'est fait ! \n connectez-vous ")
    connect()

def securite():
    print(" Bienvenue !!\n")
    choix=input(" Tapez (1) pour vous connecter \n\n Tapez (2) pour vous Inscrire \n\n---> ")
    while choix!='1' and choix!='2':
        choix=input(" Tapez (1) pour vous connecter \n\n Tapez (2) pour vous Inscrire \n\n---> ")
    if choix=='1':
        connect()
    else:
        subscribe()

securite()        

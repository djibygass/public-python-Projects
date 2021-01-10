print("Bonjour, Bienvenue Dans votre convertisseur")
    
def grand():
        
    def convers_bin():
        r=''
        nb=input("Entrer un nombre : ")
        while nb.isdigit()==False:
            nb=input("Entrer un nombre : ")
        n=int(nb)
        if n%2==0:
            while n//2!=0:
                n=n//2
                #print(n)
                r=str(n%2)+r
            r=r+'0'
            #print(n)
            print("--->",r)
            
        else:
            while n//2!=0:
                n=n//2
                #print(n)
                r=str(n%2)+r
            r=r+'1'
            #print(n)
            print("--->",r)
      
        another_one=input("Voulez-vous recommencer ? y or n : ")
        while another_one!='Y' and another_one!='y' and another_one!='N' and another_one!='n' :
            another_one=input("y or n : ")
        if another_one=='y' or another_one=='Y':
            return convers_bin()
        else:
            exit



    def convers_dec():
        check_bin='no'
        while check_bin=='no':
            nb=input("Entrer le nombre en base 2 : ")
            test=0
            for i in nb:
                if i!='0' and i!='1':
                    test+=1    
            if test==0:
                check_bin='ok'
            else:
                print("Ce nombre n'est pas binaire")
        nb=list(nb)
        s=len(nb)
        nb.reverse()
        val=0
        for i in range(0,s):
            if nb[i]=='1':
                a=nb.index(nb[i])
                #print(a)
                val+=2**a
                nb[i]=0
        print("--->",val)
            

    def conv_hexa():
        r=''
        nb=input("Entrer le nombre = ")
        n=int(nb)
        while n//16!=0:
            nn=n%16
            if nn==10:
                nn='A'
                r=str(nn)+r
            elif nn==11:
                nn='B'
                r=str(nn)+r
            elif nn==12:
                nn='C'
                r=str(nn)+r
            elif nn==13:
                nn='D'
                r=str(nn)+r
            elif nn==14:
                nn='E'
                r=str(nn)+r
            elif nn==15:
                nn='F'
                r=str(nn)+r
            else:
                r=str(nn)+r
            n=n//16
        nn=n%16
        r=str(nn)+r
        print(r)
            
            
            

        








    
    choix=input("Que voulez-vous faire ?\n\nTapez 1 Pour convertir du décimal en binaire\n\nTapez 2 Pour convertir du binaire en décimal\n\nTapez 3 Pour convertir du décimal en Héxadécimal\n\nTapez 4 Pour quitter\n\n ---> ")
    while choix!='1' and choix!='2' and choix!='3' and choix!='4':
        choix=input("Que voulez-vous faire ?\n\nTapez 1 Pour convertir du décimal en binaire\n\nTapez 2 Pour convertir du binaire en décimal\n\nTapez 3 Pour convertir du décimal en Héxadécimal\n\nTapez 4 Pour quitter\n\n ---> ")
    if choix=='1':
        convers_bin()
    elif choix=='2':
        convers_dec()
    elif choix=='3':
        conv_hexa()
    while choix!='4':
        return grand()




grand()            
#try hexa and octo

    

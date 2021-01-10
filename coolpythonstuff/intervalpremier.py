
def estpremier(nb):
    #liste=[]
    count=0
    for i in range (1,nb+1):
        if nb%i==0:
            count+=1
            #print(nb,"=",i,"*",nb//i)
    if count==2:
        #print("premier")
        #liste.append(nb)
        return True
        
        #
        print(liste)
    else:
       # print("Pas premier") 
        return False
    
    


co=0
liste=[]
nb1=input("Entrer la borne inférieure de l'intervalle : ")
nb1=int(nb1)
nb2=input("Entrer la borne supérieure de l'intervalle : ")
nb2=int(nb2)
#count=0
for nb in range (nb1,nb2+1):
    if estpremier(nb)==True:
        co+=1
        liste.append(nb)
print("Entre",nb1,"et",nb2,"Il y a",co,'nombres premiers')
print(liste)
        
        
    

    


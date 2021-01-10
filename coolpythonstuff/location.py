print("Bonjour vous avez loué une voiture")

#possibilité d'entrée (e E),(c C), (l L)
cat=input("indiquer la catégorie (E)écologique (C)confort (L)luxe : ") 
while cat!='e' and cat!='E' and cat!='c' and cat!='C' and cat!='L' and cat!='l':
    cat=input("Erreur, indiquer la catégorie (E)écologique (C)confort (L)luxe : ")   
if cat=='e' or cat=='E':
    prixjours=30
elif cat=='c' or cat=='C' :
    prixjours=50
else:
    prixjours=75

#nombre de jours compris entre (0,30)    
nbjrs=int(input("indiquer le nombre de jours : "))
while nbjrs<0 or nbjrs>30:
    nbjrs=int(input("Erreur, indiquer le nombre de jours : "))
#nombre de kilomètre
nbkm=int(input("combien de kilomètre avez-vous fait ? "))
while nbkm<0:
    nbkm=int(input("Erreur, combien de kilomètre avez-vous fait ? "))


nbkmab=0#nbre de kilomètre avec bonus
prixsupp=0#prix supplémentaire
if nbjrs>=7:
    if nbjrs==30:
        kmreg=5000#kilomètre reglementaire
        if nbkm>kmreg:
                prixsupp=(nbkm-kmreg)*0.5#chaq kilomètre en plus lui coute 0.5€
        prixtot=(nbjrs*prixjours)+prixsupp
    else:
        nbjrsi=nbjrs
        while nbjrs>=7:
            nbkmab+=1000
            nbjrs-=7
        kmreg=nbjrs*100
        kmreg+=nbkmab
        #print("avecbonus ",nbkmab,"km")
        #print("kmreg ",kmreg,"km")
        if nbkm>kmreg:
            prixsupp=(nbkm-kmreg)*0.5
        prixtot=(nbjrsi*prixjours)+prixsupp

else:
    prixtot=nbjrs*prixjours
        
      
print("le prix total est : ",prixtot,"€")


nb=-1
count=0
while nb<0:
    nb=int(input("Entrer un entier Positif : "))
while nb%2==0:
    nb/=2
    count+=1

print("le nombre choisi est divisible",count,"fois successivement par 2")
    

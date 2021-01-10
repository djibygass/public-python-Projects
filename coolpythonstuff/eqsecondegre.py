import math 
print("Ce programme traite l'équation du second degré")

a=int(input("entrer le premier coefficient : "))
b=int(input("entrer le deuxièmee coefficient : "))
c=int(input("entrer le deuxièmee coefficient : "))
delta=b*b-4*a*c
if a==0 and b==0 and c==0:
    print("La solution est R")
elif a==0 and b==0 and c!=0:
    print("Ensemble Vide")
elif a==0 and b!=0 and c!=0:
    print("On a une equation du 1er degré, la solution est ",-c/b)
else:
    if delta<0:
        print("pas de solution réelles")
    elif delta==0:
        s=(-b)/(2*a)
        print("la solution : ",s,)
    elif delta>0:
        x1=(-b-math.sqrt(delta))/(2*a)
        x2=(-b+math.sqrt(delta))/(2*a)
        print("les solutions sont x1 = ",x1,"x2 = ",x2)

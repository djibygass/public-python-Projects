print("Bonjour, Bienvenu.\n")
print("Ce programme donne un jour de semaine à une date Rentrée....(jj/mm/aaaa)")

mois=int(input("Entrer le mois : "))
while 0<mois<=12 and mois.isdigit()==False:
    mois=int(input("Entrer le mois : "))    
an=int(input("Entrer l'année : "))
while 0<an<=12 and an.isdigit()==False:
    an=int(input("Entrer l'année : "))
    
jour=int(input("Entrer le jour : "))
while 0<jour<=12 and jour.isdigit()==False:
    jour=int(input("Entrer le jour : "))



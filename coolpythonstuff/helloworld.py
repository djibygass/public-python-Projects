#par djibril le 09/01/2020
"""c'est du com aussi mais sur plusieur ligne"""
print("hello world!! \n what's up")

age=int(input("Entrer votre age : "))


nom=input("quel est votre nom : ")

print("Bonjour",nom,"vous avez",age,"ans")

if age >= 70:
    print("senor.")
elif age >= 60:
    print("retraite.")
elif age >= 18:
    print("permis.")
else:
    print(" mineur..")
if nom=="Djibril" and age>=60:
    print("1000 balles")

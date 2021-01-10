nb1=int(input("Entrer un nombre : "))
op=input("Entrer l'opération + - / ou * : ")
nb2=int(input("Entrer un nombre : "))

if op == '+' :
    print("le résultat est : ",nb1+nb2)
elif op == '-' :
    print("le résultat est : ",nb1-nb2)
elif op == '/' and nb2!=0:
    print("le résultat est : ",nb1/nb2)
elif op == '/' and nb2==0:
    print("Error")
elif op == '*' :
    print("le résultat est : ",nb1*nb2)

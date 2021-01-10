#fonction ouvrir
chemin="C:\\Users\\Administrateur\\AppData\\Local\\Programs\\Python\\Python38-32\\contact.txt"
def ouvrir(chemin):
    f=open(chemin,"a")

def fermer(chemin):
    f.close()

ouvrir(chemin)
f.write=("SALUT")
fermer()

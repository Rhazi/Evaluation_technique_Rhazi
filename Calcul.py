import queue_cl
stack = [] # liste vide = stack
teteStack = 0 #tete stack
tailleStack = 6 #taille stack
Operateurs=("+","-","*","/") #operateurs

def StackAjout(element):
    "Ajout element en queue du stack si non rempli en entier + incrementation teteStack"
    global stack, teteStack
    if teteStack < tailleStack:
        stack.append(element)
        teteStack +=1
        print("Stack:",stack)
    else:
        print("stack rempli")

def StackSupprime():
    "Retourne et supprime tete stack + decrementation teteStack"
    global stack, teteStack
    elementSupprime = None
    if teteStack >=1:
        teteStack -=1
        elementSupprime = stack.pop(teteStack)
    else:
        print("stack vide")
    return elementSupprime

def Somme(val1, val2):
    "Somme des valeurs"
    return val1 + val2

def Soustraction(val1, val2):
    "Difference des valeurs"
    return val1 - val2

def Multiplier(val1, val2):
    "Produit des valeurs"
    return val1*val2

def Division(val1, val2):
    "Division des valeurs"
    return val1/val2


def equations(operateur):
    "equation sur des valeurs de la pile, effectuee avec l'operateur rajoutee en fin de stack. Retourne l'operation"
    global Operateurs
    val1 =None
    val2 =None
    valFinale = None

    #si l operateur est valable
    if operateur not in Operateurs:
        print ("L'operateur",operateur, "n'est pas valable")
    else: #si l'operateur est ok, on opere sur les deux valeurs de la pile a partir de la droite
        val1 = StackSupprime()
        val2 = StackSupprime()
        if val1 == None or val2 == None:
            print("stack pas assez rempli")
        else:
            if operateur == Operateurs[0]:
                valFinale=Somme(val1,val2)
            elif operateur == Operateurs[1]:
                valFinale=Soustraction(val1,val2)
            elif operateur == Operateurs[2]:
                valFinale=Multiplier(val1,val2)
            elif operateur == Operateurs[3]:
                valFinale=Division(val1,val2)
            else:
                print("L'operateur",operateur, "n'est pas valable")

    return valFinale


def ChunkString(monString):
    "Prends une chaine de caracteres en arguments. Check l'existence d'un operateur, "
    'le cas echeant, applique la fonction equations pour le calcul sinon rien'
    valFinale = None #variable locale
    operateur = None

    monString = monString.replace(" ", "")
    listeString = monString.split(",")
    tempString=""
    for i in range(0,len(listeString)):
        if unicode(listeString[i]).isnumeric():
            StackAjout(float(listeString[i]))
        else:
            for element in listeString[i]:
                if unicode(element).isnumeric():
                    tempString+=element
                else:
                    queue_cl.Ajoutequeue(element)

            if len(tempString)>0:
                StackAjout(float(tempString))


    while queue_cl.queueSize() > 0:
        operateur = queue_cl.Supprimequeue()
        valFinale = equations(operateur)
        if valFinale != None:
            StackAjout(float(valFinale))
    return valFinale




def menu():
    "Fonction applicative"

    print("Veuillez rentrer votre operation au format RPN")
    while True:
        try:
            monString = ""
            StringSortie ="Le resultat de"
            monString = input("Rentrer votre equation RPN")
            if monString == "exit":
                break
            print("Votre selection", monString)
            valFinale = ChunkString(monString)
            StringSortie += monString + " est " + str(valFinale)
            print(StringSortie)
        except KeyboardInterrupt:
            break

if __name__ =="__main__":
    menu()

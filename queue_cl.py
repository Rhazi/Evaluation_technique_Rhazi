"variables globales"
queue = []
queueTaille = 5 #fixer la valeur max de queue
queueElt = 0

def queueSize():
    global queue
    return len(queue)


def Ajoutequeue(element):
    "Ajoute un element a queue"
    global queue, queueTaille, queueElt
    if queueElt < queueTaille:
        queue.append(element)
        print("queue actuelle:", queue)
    else:
        print("queue remplie")


def Supprimequeue():
    global queue, queueTaille, teteStack, queueElt
    elementSupp = None
    if len(queue)>0:
        elementSupp = queue.pop(0)
        print("queue actuelle:", queue)
    else:
        print("Queue vide!")
    return elementSupp


if __name__ =="__main__":

    Ajoutequeue("+")
    Ajoutequeue("*")
    print(Supprimequeue())
    Ajoutequeue("-")
    print(Supprimequeue())
    print(Supprimequeue())
    print(Supprimequeue())

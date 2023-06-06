def pairWiseConsecutive(l):
    aux = []
    while (len(l)!=0):
        aux.append(l.pop())
    while len(aux)>1:
        x = aux.pop()
        y = aux.pop()
        if abs(x-y)!=1:
            return False
    return True

l = [1 ,2 ,3 ,4 ,5 ,6]

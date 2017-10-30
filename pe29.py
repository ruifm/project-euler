k=100
lista=[]
for a in xrange(2,k+1):
    for b in xrange(2,k+1):
        if a**b not in lista:
            lista.append(a**b)
        elif b**a not in lista:
            lista.append(b**a)

print len(lista)



def crivo(k):
    conjunto=range(3,k,2)
    conjunto.insert(0,2)
    for i in xrange(len(conjunto)):
        f=open("results.txt", "w")
        f.write(str(conjunto[i]))
        f.close()
        conjunto=conjunto[:i+1]+filter(lambda y: y%conjunto[i]!=0, conjunto[i:])
    return conjunto

crivo(2000000)
input('fnished')

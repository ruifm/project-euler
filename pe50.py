def crivo(k):
    conjunto=range(2,k)
    for x in conjunto:
        for i in conjunto:
            if i%x==0 and i>x:
                conjunto.remove(i)
    return conjunto
target=100
somas=[]
conjunto=crivo(target)

def f(n,s):
    if n == 1:
        return [s]
    else:
        for i in crivo(s):
            for j in f(n - 1,s - i):
                return [i] + [j]
    


for x in conjunto:
    for n in range(2,conjunto.index(x)):
        somas.append(f(n,x))
        print somas
            

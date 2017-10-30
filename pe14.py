print 'PE problem 14: '
answer=[]
def tran(n):
    conjunto=[]
    while n>1:
        if n%2==0:
            n=n/2
            conjunto.append(n)
            tran(n)
        else:
            n=3*n+1
            conjunto.append(n)
            tran(n)
    if n==1:
        resultado=len(conjunto)+1
        return resultado

total=range(500001,1000000,2)

    
for n in total:
    print n
    answer.append(tran(n))
    if tran(n)>=max(answer):
        print 'new result: ', n

input('finished')


    

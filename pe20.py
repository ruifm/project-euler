def factorial(n):
    r= n
    while n>1:
        n += -1
        r=r*n
    return r

a=str(factorial(100))
b=list(a)
c=[]
for i in range(len(b)):
    c.append(int(b[i]))



print sum(c)

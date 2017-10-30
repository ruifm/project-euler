a=2**100
b=str(a)
c=list(b)
d=[]
for i in range(len(c)):
    d.append(int(c[i]))

print sum(d)

x=2
soma=0
while x<(9**5)*len(str(x)):
    if x==sum(map(lambda y: y**5, map(lambda z: int(z),list(str(x))))):
        print x
        soma+=x
    x+=1

print soma

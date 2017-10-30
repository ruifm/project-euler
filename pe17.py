def value1(z):
    t=int(z)
    if t==1:
        return 3
    if t==2:
        return 3
    if t==3:
        return 5
    if t==4:
        return 4
    if t==5:
        return 4
    if t==6:
        return 3
    if t==7:
        return 5
    if t==8:
        return 5
    if t==9:
        return 4
    if t==0:
        return 0

def value2(z):
    t=int(z)
    if t==1:
        return 3
    if t==2:
        return 6
    if t==3:
        return 6
    if t==4:
        return 5
    if t==5:
        return 5
    if t==6:
        return 5
    if t==7:
        return 7
    if t==8:
        return 6
    if t==9:
        return 6
    if t==0:
        return 0

def value3(z):
    t=int(z)
    if t==1:
        return 3+10
    if t==2:
        return 3+10
    if t==3:
        return 5+10
    if t==4:
        return 4+10
    if t==5:
        return 4+10
    if t==6:
        return 3+10
    if t==7:
        return 5+10
    if t==8:
        return 5+10
    if t==9:
        return 4+10
    if t==0:
        return 0

def value4(z):
    t=int(z)
    if t==1:
        return 6
    if t==2:
        return 6
    if t==3:
        return 8
    if t==4:
        return 8
    if t==5:
        return 7
    if t==6:
        return 3+4
    if t==7:
        return 5+4
    if t==8:
        return 5+3
    if t==9:
        return 4+4
    if t==0:
        return 0

def number(x):
    y=str(x)
    if len(y)==3:
        if y[1]=='1' and y[2]!='0':
            soma=value3(y[0])+value4(y[2])
        else:
            soma=value3(y[0])+value2(y[1])+value1(y[2])
    if len(y)==2:
        if y[0]=='1' and y[1]!='0':
            soma=value4(y[1])
        else:
            soma=value2(y[0])+value1(y[1])
    if len(y)==1:
        soma=value1(y)
    if len(y)==4:
        soma=3+8
    return soma

resultado=0
for element in xrange(1,1001):
    resultado+=number(element)

print resultado-3*9 #nos numeros 100, 200, 300...900 contei um 'and' a mais

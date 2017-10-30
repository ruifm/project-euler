f=open("names.txt", "rU")
names=sorted(f.read().replace('"','').split(','), key=str)
def lvalue(x):
    if x=='A':
        return 1
    if x=='B':
        return 2
    if x=='C':
        return 3
    if x=='D':
        return 4
    if x=='E':
        return 5
    if x=='F':
        return 6
    if x=='G':
        return 7
    if x=='H':
        return 8
    if x=='I':
        return 9
    if x=='J':
        return 10
    if x=='K':
        return 11
    if x=='L':
        return 12
    if x=='M':
        return 13
    if x=='N':
        return 14
    if x=='O':
        return 15
    if x=='P':
        return 16
    if x=='Q':
        return 17
    if x=='R':
        return 18
    if x=='S':
        return 19
    if x=='T':
        return 20
    if x=='U':
        return 21
    if x=='V':
        return 22
    if x=='W':
        return 23
    if x=='X':
        return 24
    if x=='Y':
        return 25
    if x=='Z':
        return 26
def wvalue(word):
    soma=0
    for s in xrange(len(word)):
        soma+=lvalue(word[s])
    return soma
        
valores=[]
for i in xrange(len(names)):
    valores.append(wvalue(names[i])*(i+1))

print sum(valores)
    
    

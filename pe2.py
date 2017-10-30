n=0
s=1
soma=0
while n+s<4000000:
    n += s
    s += n
    if n%2==0:
        soma += n
    if s%2==0:
        soma += s
        

print soma

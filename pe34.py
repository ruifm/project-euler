
def factorial(n):
    if n==0 or n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 6
    if n==4:
        return 24
    if n==5:
        return 120
    if n==6:
        return 720
    if n==7:
        return 5040
    if n==8:
        return 40320
    if n==9:
        return 362880

x=0
soma=0
while x<factorial(9)*len(str(x)):
    if x==sum(map(lambda y: factorial(y),(map(lambda y: int(y),list(str(x)))))):
        print x
        soma += x
    x += 1
    
print 'The answer is: ', soma -2 -1
input('finished')
        
    

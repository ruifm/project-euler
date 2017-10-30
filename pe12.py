print 'PE problem 12:'
def primes(s):
    n=2
    if s == 2 or s==3:
        return True
    elif s < 1:
        return 'out of Domain'

    elif s==1 or s==4:
        return False
    else:
        while n<s-1:
            n += 1
            if s%n==0:
                control=False
            else:
                control=True
            if control==False:
                return False
        return True


divisores=0

target=500
n=0
soma=0

answer=[]

def divisors(r):
    d=1
    divisores=1
    if primes(soma)==False:
        while d<=soma/2:
            if soma%d==0:
                divisores += 1
            d += 1
    return divisores

while len(answer)<=0:
    soma += n
    if divisors(soma)>target:
        print 'The answer is: ',soma
        break
    n += 1            
input('finished')
        

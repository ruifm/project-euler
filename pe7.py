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

primos=[]


def listing(n):
    while n>=0:
        if primes(n)==True:
            primos.append(n)
        if len(primos)==10001:
            return primos[10000]
        n += 1
print listing(1)


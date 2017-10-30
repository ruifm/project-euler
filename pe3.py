target = input('Insert number to find prime factors: ')

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

def primes2(r):
    while r <= target/2:
        r += 1
        if primes(r)==True and target%r==0:
            print r
    print 'game over'
while 1:
    primes2(1)
    target=input('Insert number to find prime factors: ')

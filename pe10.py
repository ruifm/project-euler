#atencao! algoritmo muito lento. demorou cerca de 12h30 a obter a solucao...
#sugestao: implementar o crivo de earistofenes, em vez da funcao primes

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


l=1
soma=0
progress=1
target=2000000
percentage=(target/100)*progress

while l<target:
    print l
    if primes(l)==True:
            soma += l
    l += 2


print 'The answer is ', soma+2 #porque nao considerou o 2, 1o numero primo

input('wait')

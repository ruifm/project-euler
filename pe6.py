def square(x):
    return x*x

hundred=range(1,101)

conjunto=[]
def allsquares():
    for x in hundred:
        conjunto.append(square(x))
    return sum(conjunto)
    


answer=square(sum(hundred)) - allsquares()

print answer

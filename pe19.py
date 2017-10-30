leap=0
def counter(year):
    k=0
    resultado=0
    if year%4==0:
        duration=366
    else:
        duration=365
    if year==1901:
        k=0
    else:
        if (year-1)%4==0:
            k=year-1901+leap
        else:
            k=year-1901+leap
    sunday=6-k
    while sunday<=duration:
        if sunday>0 and duration==365:
            if sunday==1 or sunday==32 or sunday==60 or sunday==91 or sunday==121 or sunday==152 or sunday==182 or sunday==213 or sunday==244 or sunday==274 or sunday==305 or sunday==335:
                resultado+=1
        if sunday>0 and duration==366:
            if sunday==1 or sunday==32 or sunday==61 or sunday==92 or sunday==122 or sunday==153 or sunday==183 or sunday==214 or sunday==245 or sunday==275 or sunday==306 or sunday==336:
                resultado+=1
        sunday+=7
    return resultado
soma=0
for year in xrange(1901,2001):
    if year!=1901 and (year-1)%4==0:
        leap+=1
    soma+=counter(year)

print soma

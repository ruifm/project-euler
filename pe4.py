
resultados=[]
def capicua(factor1):
    factor2=101
    while factor1<=999 and factor2<=999:
        target=factor1*factor2
        if str(target)[0]==str(target)[-1] and str(target)[1]==str(target)[-2] and str(target)[2]==str(target)[-3]:
            resultados.append(target)
        factor2 += 1
    
test=100
while 100<=test<1000:
    capicua(test)
    if not resultados==[]:
        max(resultados)
        

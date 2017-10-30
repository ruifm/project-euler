# -*- coding: cp1252 -*-

triplet=[] 
thetriplet=[]

def finding(b): # encontra tripletos
    a=1
    while a<=1000.:
        a += 1
        c=(((a)**(2)) + ((b)**(2)))**(0.5)
        if c in range(1,1001):
            triplet.append([a,b,int(c)]) # passo para formar triplet
            
                
        
for b in range(1,1000): # formar a lista triplet completa
    finding(b)

for index in range(len(triplet)): # formar thetriplet (lista de somas)
    thetriplet.append(sum(triplet[index]))

def indexfinder(): #supostamente serve para encontrar o index com o tripleto da solucao
    for tracker in range(len(thetriplet)):
        if thetriplet[tracker]==1000:
            return tracker

answer=triplet[indexfinder()][0]*triplet[indexfinder()][1]*triplet[indexfinder()][2]

print answer
input('wait')

a=[0]*15
a[0]=[75]
a[1]=[95,64]
a[2]=[17,47,82]
a[3]=[18,35,87,10]
a[4]=[20,4,82,47,65]
a[5]=[19,1,23,75,3,34]
a[6]=[88,02,77,73,07,63,67]
a[7]=[99,65,4,28,6,16,70,92]
a[8]=[41,41,26,56,83,40,80,70,33]
a[9]=[41,48,72,33,47,32,37,16,94,29]
a[10]=[53,71,44,65,25,43,91,52,97,51,14]
a[11]=[70,11,33,28,77,73,17,78,39,68,17,57]
a[12]=[91,71,52,38,17,14,91,43,58,50,27,29,48]
a[13]=[63,66,04,68,89,53,67,30,73,16,69,87,40,31]
a[14]=[04,62,98,27,23,9,70,98,73,93,38,53,60,4,23]

results=[]

def func(index):
    i=13
    soma=a[14][index]
    soma2=a[14][index]
    while i>=0:
        if index==0:
            soma+=a[i][index]
        elif index>0:
            soma+=a[i][index-1]
            func(index-1)
            if index!=len(a[i]):
                soma2+=a[i][index]
        elif index==len(a[i]):
            soma+=a[i][index-1]
        i += -1
        index+=-1
    results.append(soma)
    results.append(soma2)

for index in range(len(a[14])):
    func(index)

print max(results)
        

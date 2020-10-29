
n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11,1]
i=0
b=[]
while(i<len(n)):
    j=i+1
    while(len(n)>j):
        if(n[i]==n[j]):
            if(n[i] not in b):
                b.append(n[i])
                break
        j=j+1
    i=i+1
print(b)
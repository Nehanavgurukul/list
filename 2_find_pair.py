number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19]
i=0
b=[]
l=[]
while(i<len(n)):
    j=1
    while(j<len(n)):
        if(n[j] not in l):
            l.append(n[i])
            if(n[i]+n[j]==number):
                c=[n[i],n[j]]
                b.append(c)
        j=j+1
    i=i+1
print(b)

n=[-3,-2,-5,-9,-7,-1]
i=0
max_num=n[0]
while(i<len(n)):
    if(max_num<=n[i]):
        max_num=n[i]
    i=i+1
print(max_num)

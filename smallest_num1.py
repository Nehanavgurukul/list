n=[-3,-2,-5,-9,-7, -32,-12]
i=0
smallest_num=0
while(i<len(n)):
    if(smallest_num>n[i]):
        smallest_num=n[i]
    i=i+1
print(smallest_num)
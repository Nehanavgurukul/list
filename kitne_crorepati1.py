kitne_crorepati_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
k_c=0
l_c=0
d_c=0
while(i<len(kitne_crorepati_hai)):
    if(kitne_crorepati_hai[i]>=10000000):
        k_c=k_c+1
    elif(kitne_crorepati_hai[i]>=100000):
        l_c=l_c+1
    else:
        d_c=d_c+1
    i=i+1
print(k_c)
print(l_c)
print(d_c)

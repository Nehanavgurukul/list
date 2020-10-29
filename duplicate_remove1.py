a = [10,20,30,20,10,50,60,40,80,50,40]
i=0
list=[]
while(i<len(a)):
    if a[i] not in list:
        list.append(a[i])
    i=i+1
print(list)
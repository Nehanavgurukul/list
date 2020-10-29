n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]


index=0
list=[]
while(index<len(n)):
    j=index+1
    while(j<len(n)):
        if(n[index]==n[j]):
            if(n[index] not in list):
                list.append(n[index])
        j=j+1
    index=index+1
print(list)
    
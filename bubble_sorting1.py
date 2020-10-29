list =[3,5,1,34,56,24,678,34,1,67,9,567,0,674]
i=0
while(i<len(list)):
    j=0
    while(j<i):
        if(list[i] <list[j]):
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
        j=j+1
    i=i+1
print(list)


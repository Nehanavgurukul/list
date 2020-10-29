num=[78,23,50,98,56,20,11,70,55]
index=0


while(index<len(num)):
    j=0
    while(j<len(num)):
        if(num[index]>num[j]):
            tamp=num[index]
            num[index]=num[j]
            num[j]=tamp
        j=j+1
    index=index+1
print(num)
l=[3,5,1,4]
i=0
# a=[]
while(i<len(l)):
    j=0
    while(j<i):
        if(l[i] <l[j]):
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
        j=j+1
    i=i+1
print(l)


      
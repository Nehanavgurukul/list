list=[50, 40, 23, 34,26,38,70, 56, 12, 5, 10, 7]
index=0
l=[]
while(index<len(list)):
    if(list[index]>20 and list[index]<40):
        l.append(list[index])
    index=index+1
print(l)
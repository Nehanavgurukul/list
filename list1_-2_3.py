index=1
list=[]
while(index<=10):
    if(index%2==0):
        list.append(-index)
        
    else:
        list.append(index)
        
    index=index+1
print(list)

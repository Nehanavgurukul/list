a = [10,20,30,20,10,50,60,40,80,50,40]
i=0
uniq_list=[]
dupli_list=[]
while(i<len(a)):
    if a[i] not in uniq_list:
        uniq_list.append(a[i])
    else:
        dupli_list.append(a[i])
    
    i=i+1
print(uniq_list)
print(dupli_list)
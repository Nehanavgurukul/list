n=[1,45,7,45,576,876,87,58,3,86,34,0,9,17]
i=0
max_num=0
while(i<len(n)):
    if(max_num<n[i]):
        max_num=n[i]
    i=i+1  
print(max_num)
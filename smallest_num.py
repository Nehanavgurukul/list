n=[1,45,7,45,87,58,3,86,34,9,17]
i=0
smallest_num=n[i]
while(i<len(n)):
    if(smallest_num>n[i]):
        smallest_num=n[i]
    i=i+1   
print(smallest_num)
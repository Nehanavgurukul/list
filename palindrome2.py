first_list=["neha","rinki","pooja","radha","pooja","rinki","neha"]
last_list=[]

i=len(first_list)-1
while(i>=0):
    last_list.append(first_list[i])
    i=i-1
if(first_list==last_list):
    print("it is  palindrome")
else:
    print("it is not  palindrome")
    
    
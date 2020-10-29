elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
sum_e=0
sum_o=0
i=0
while(i<len(elements)):
    if(elements[i]%2==0):
        sum_e=sum_e+1
    else:
        sum_o=sum_o+1
    i=i+1
print("even " ,sum_e ,"the")
print("odd" ,sum_o ,"the")
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
sum_e=0
sum_o=0
i=0
while(i<len(elements)):
    if(elements[i]%2==0):
        sum_e=sum_e+elements[i]
    else:
        sum_o=sum_o+elements[i]
    i=i+1
print("even sum " ,sum_e ,"tha")
print("odd sum" ,sum_o ,"tha")
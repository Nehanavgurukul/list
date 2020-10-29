elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
s_e=0
s_o=0
while(i<len(elements)):
    if(elements[i]%2==0):
        s_e=s_e+elements[i]
    else:
        s_o=s_o+elements[i]
    i=i+1
print(s_e)
print(s_o)
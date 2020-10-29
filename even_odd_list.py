elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
c_e=0
c_o=0
while(i<len(elements)):
    if(elements[i]%2==0):
        c_e=c_e+1
    else:
        c_o=c_o+1
    i=i+1
print(c_e)
print(c_o)
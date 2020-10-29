elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
c_even=0
c_odd=0
s_even=0
s_odd=0
index=0
while(index<len(elements)):
    if(elements[index]%2==0):
        c_even=c_even+1
        s_even=s_even+elements[index]
    else:
        c_odd=c_odd+1
        s_odd=s_odd+elements[index]
    index=index+1
print("even hai",c_even)
print("odd hai",c_odd)
print("even sum",s_even)
print("odd sum", s_odd)
print("even average",s_even//c_even)
print("odd average",s_odd//c_odd)

# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# c_even=0
# c_odd=0
# s_even=0
# s_odd=0
# index=0
# while(index<len(elements)):
#     if(elements[index]%2==0):
#         c_even=c_even+1
#         s_even=s_even+elements[index]
#     else:
        
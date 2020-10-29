magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]

i=0

while(i==0):
    j=0
    sum=0
    while(j<len(magic_square)):
        sum=sum+magic_square[i][j]
        j=j+1
    sums.append(sum)
    j=0
    sum=0
    while(i<len(magic_square)):
        sum=sum+magic_square[i][j]
        i=i+1
    sums.append(sum)
    i=0
    j=0
    sum=0
    while(i<len(magic_square)):
        sum=sum+magic_square[i][j]
        j=j+1
        i=i+1
    sums.append(sum)
for i in range(len(sums)):
    if(sums[i]==sum):
        print("it is magic_square")
    else:
        print("it is not magic_square")



# list = [
#     [8, 3, 4],
#     [1, 5, 9],
#     [6, 7, 2]
# ]
# i=0
# while(i<len(list)):
#     sum1=0
#     j=0
#     while(j<len(list[i])):
#         sum1=sum1+list[i][j]
#         j=j+1
#     print(sum1)
#     sum2=0
#     j=0
#     while(i<len(list)):
#         sum2=sum2+list[i][j]
#         i=i+1
#     print(sum2)
#     j=0
#     i=0
#     sum3=0
#     while(i<len(list)):
#         sum3=sum3+list[i][j]
#         i=i+1
#         j=j+1
#     print(sum3)
# if(sum1==sum2 and sum2==sum3):
#     print("it is magic square")
# else:
#     print("it is not magic square")


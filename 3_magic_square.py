magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
i=0
sums=[]
while(i<len(magic_square)):
    sum=0
    j=0
    while(j<len(magic_square[i])):
        sum=sum+magic_square[i][j]
        j=j+1
    sums.append(sum)
    i=i+1
i=0
while(i<len(magic_square)):
    j=0
    sum=0
    while(j<len(magic_square)):
        sum=sum+magic_square[j][i]
        j=j+1
    sums.append(sum)
    i=i+1
i=0
j=0
sum=0
while(j<len(magic_square)):
    sum=sum+magic_square[i][j]
    i=i+1
    j=j+1
sums.append(sum)

for i in range(len(sums)):
    if(i==sum):
        print("magic_square hai")
    else:
        print("magic_square nhi hai")
        
    




# magic_square = [
#     [8, 3, 4],
#     [1, 5, 9],
#     [6, 7, 2]
# ]
# i=0
# sums=[]
# while(i<len(magic_square)):
#     sum=0
#     j=0
#     while(j<len(magic_square[i])):
#         sum=sum+magic_square[i][j]
#         j=j+1
#     sums.append(sum)
#     i=i+1
# j=0
# while(j<len(magic_square)):
#     i=0
#     sum=0
#     while(i<len(magic_square[j])):
#         sum=sum+magic_square[j][i]
#         i=i+1
#     sums.append(sum)
#     j=j+1
    
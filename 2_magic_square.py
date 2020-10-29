magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]

i=0
sums=[]

while(i<len(magic_square)):
    j=0
    sum=0
    while(j<len(magic_square[i])):
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
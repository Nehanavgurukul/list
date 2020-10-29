binary_number = [1, 0, 0, 1, 1, 0, 1, 1]
decimal=0
c=1
length=len(binary_number)-1
while(length>=0):
    decimal=decimal+binary_number[length]*c
    c=c*2
    length=length-1
print(decimal)


marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
]
marks=marks[0]+marks[1]+marks[2]
i=0
sum=0
length=len(marks)
while(i<length):
    sum=sum+marks[i]
    i=i+1
print(sum)

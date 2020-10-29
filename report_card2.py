marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78],
    [87, 67, 49, 68, 88]
]
marks=marks[0]+marks[1]+marks[2]+marks[3]
i=0
sum=0
while(i<len(marks)):
    sum=sum+marks[i]
    i=i+1
print(sum)
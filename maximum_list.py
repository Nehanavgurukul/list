numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
max_num=0
while(i<len(numbers)):
    if(max_num<numbers[i]):
        max_num=numbers[i]
    i=i+1
print(max_num)
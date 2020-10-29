original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
b=[]
i=0
while(i<len(original_list)):
    j=0
    while(j<len(original_list[i])):
        b.append(original_list[i][j])
        j=j+1
    i=i+1
print(b)

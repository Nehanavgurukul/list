char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
b=[]
i=0
while(i<len(char_list)):
    count=0
    j=0
    while(j<len(char_list)):
        if(char_list[i]==char_list[j]):
            count=count+1
        j=j+1
    c=[char_list[i],count]
    if([char_list[i],count]not in b):
        b.append(c)
    i=i+1
print(b)
    
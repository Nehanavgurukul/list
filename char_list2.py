char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
index=0
list=[]
while(index<len(char_list)):
    count=0
    j=0
    count=0
    while(j<len(char_list)):
        if(char_list[index]==char_list[j]):
            count=count+1
        j=j+1
    c=[char_list[index],count]
    if(c not in list):
        # c=[char_list[i],count]
        list.append(c)
    index =index +1
print(list)
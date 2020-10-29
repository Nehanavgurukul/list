string="i am string"
i=0
new_list=[]
a=''
while(i<len(string)):
    if(string[i]==' '):
        new_list.append(a)
        a=' '
    else:
        a=a+string[i]
    i=i+1
new_list.append(a)
print(new_list)
sentence = "NavGurukul is an alternative to higher education reducing the barriers of current formal education system"
counter = 0
list=[]
a=" "
while(counter < len(sentence)):
    if(sentence[counter]==" "):
        list.append(a)
        a=" "
        counter=counter+1
    else:
        # list.append(sentence[counter])
        a=a+sentence[counter]
        counter=counter+1
print(list)
        
    




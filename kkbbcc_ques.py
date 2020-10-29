question_list = [
    "How many continents are there?",             
    "What is the capital of India?",        
    "NG mei kaun se course padhaya jaata hai?" 
]

options_list = [
    #pehle question ke liye options
    ["Four", "Nine", "Seven", "Eight"],
    #second question ke liye options
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    #third question ke liye options
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
solution_list = [3, 4, 1]

i=0

while(i<len(question_list)):
    print(question_list[i])
    j=0
    while(j<len(options_list[i])):
        print((j+1),'.',options_list[i][j])
        j=j+1
    user=int(input("enter the ans"))
    index=0
    while(index<len(solution_list)):
        print(solution_list[index])
        if(user == solution_list[index]):
            print("congrats! your ans absolutly right ,you won ")
            break
        else:
            print(" sadly your ans wrong ,you are out of game ")
        break
    break
    i=i+1
    
        
question_list = [
    "How many continents are there?",           
    "What is the capital of India?",            
    "NG mei kaun se course padhaya jaata hai?"   
]

options_list = [
    ["Four", "Nine", "Seven", "Eight"],
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]

# har ek question ke liye, uski solution key (yeh index nahi hai)
solution_list = [3, 4, 1]


index1=0
while(index1<len(question_list)):
    print((index1+1),".",question_list[index1])
    # index2=0
    # while(index2<len(options_list[index1])):
    #     print((index2+1),".",options_list[index1][index2])
    #     index2=index2+1
    user_ans=int(input("enter the user ans number"))
    # i=0
    # while(i<len(solution_list)):
    if(user_ans==solution_list[index1]):
        print("apka ans sahi  right h")
        # break
    else:
        print("sorry apka ans wrong h")
        break
        
    index1=index1+1

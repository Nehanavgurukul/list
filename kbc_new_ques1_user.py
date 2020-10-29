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


index=0
while(index<len(question_list)):
    print((index+1),".",question_list[index])
    user_ans=input("enter the user ans ")
    option_ans=input("enter the option ans")
    if(user_ans==option_ans):
        print("congrats! apka ans sahi hai")
    else:
        print("sadly !apka ans galt hai")
    index=index+1
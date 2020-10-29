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


solution_list = [3, 4, 1]


index=0
while(index<len(question_list)):
    print((index+1),".",question_list[index])
    correct_ans=input("enter the correct ans ")
    j=0
    while(j<len(options_list)):
        options_ans=input("enter the options ans")
        if(correct_ans==options_ans):
            print("congrats! your ans absolutly right")
            break
        else:
            print("sadly ! your ans wrong and you went to out")
            break
    index=index+1
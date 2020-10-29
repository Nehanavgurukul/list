# question_list = [
#     "How many continents are there?",             
#     "What is the capital of India?",        
#     "NG mei kaun se course padhaya jaata hai?"    
# ]

# options_list = [
#     ["Four", "Nine", "Seven", "Eight"],
#     ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
#     ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
# ]

# index=0
# i=0
# while(index<len(question_list)):
#     print(question_list[index])
#     ans=input("enter the answer")
#     while(i<len(options_list)):
#         j=0
#         while(j<len(options_list[i])):
#             # print((j+1), options_list[i][j])
#             user_ans=input("enter the options")
#             if(ans==user_ans):
#                 print("congrats! apka ans sahi h")
#                 j=j+1
#                 break   
#             else:
#                 print("sorry apka ans sahi nhi h")
#                 j=j+1
#     index=index+1

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

index=0
i=0
while(index<len(question_list)):
    print(question_list[index])
    ans=input("enter the answer")
    user_ans=input("enter the user ans")
    if(ans==user_ans):
        print("congrats! apka ans sahi h")
    else:
        print("aap game se bahar ho")
    index=index+1
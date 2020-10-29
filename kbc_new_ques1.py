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
print(question_list[1])
index=0
while(index<len(options_list[1])):
    print((1+index),".",options_list[1][index])
    index=index+1
    









# question_list = [
#     "How many continents are there?",              # pehla question
#     "What is the capital of India?",            # doosra question
#     "NG mei kaun se course padhaya jaata hai?"    # teesra question
# ]

# options_list = [
#     #pehle question ke liye options
#     ["Four", "Nine", "Seven", "Eight"],
#     #second question ke liye options
#     ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
#     #third question ke liye options
#     ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
# ]

# # har ek question ke liye, uski solution key (yeh index nahi hai)
# solution_list = [3, 4, 1]
# print(question_list[1])
# index=0
# while(index<len(options_list[1])):
#     print((1+index),".",options_list[1][index])
#     index=index+1
    
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
    while(i<len(options_list)):
        j=0
        while(j<len(options_list[i])):
            print((j+1), options_list[i][j])
            j=j+1
        break
    i=i+1
    index=index+1
    
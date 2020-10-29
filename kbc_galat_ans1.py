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
i=0

while(i<len(question_list)):
    print(question_list[i])
    currect_ans=input("enter the currect ans.")
    j=0
    while(j<len(options_list)):
        options_ans=input("enter the option")
        if(options_ans == currect_ans):
            print("congrats! apka ans right" )
            break
        else:
            print("sorry ans wrong h aap bahar kr diye gye ho")
            break
    i=i+1    
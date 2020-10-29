# mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
# subStr = "over"
# replacementStr = "on"
# list1=mainStr.split()


# new_list=list(mainStr)
# print(new_list)
# i=0
# while(i<len(new_list)):
#     if( new_list[i]==subStr):
#         new_list[i].replacementStr("on")
#     i=i+1
# print(new_list)


mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
subStr = "over"
num=mainStr.split()
index=0
while(index<len(num)):
    if(num[index]==subStr):
        num.remove("over")
        num[index]=("on")
        # n=num.replace("over","on")
    
    index=index+1
list1='  '.join(num)
print(list1)
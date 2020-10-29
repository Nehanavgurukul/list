mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
subStr = "over"
num=mainStr.split()
index=0
while(index<len(num)):
    if(num[index]==subStr):
        num.remove("over")
    index=index+1
list1='  '.join(num)
print(list1)




# index=1
# while(index<=10):
#     if(index%2==0):
#         print(-index)
#     else:
#         print(index)
#     index=index+1

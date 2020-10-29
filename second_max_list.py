# n = [50, 40, 23, 70, 56, 12, 5, 10,54]
# i=0
# second_num=0
# max_num=0
# while(i<len(n)):
#     if(max_num<n[i]):
#         second_num=max_num
#         max_num=n[i]
#     i=i+1
# print(second_num)

# n=[1,45,7,45,576,876,87,58,3,86,34,0,9,17]
# # i=0
# # second_max=0
# # max_num=0
# # while(i<len(n)):
#     if(max_num<n[i]):
#         second_max=max_num
#         max_num=n[i]
#     i=i+1  
# print(second_max)   

list=[24,56,67,34,89,23,57,95]
sec_max=0
max=0
i=0
while(i<len(list)):
    if(max<list[i]):
        max=list[i]
    i=i+1
print(max)
j=0
while(j<len(list)):
    if(sec_max<list[j]and list[j]<max):
        sec_max=list[j]
    j=j+1
print(sec_max)




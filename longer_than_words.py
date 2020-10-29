list="The quick brown fox jumps over the lazy dog"
a=list.split()

b=[]
n=4
for x in a:
    if(len(x)>n):
        b.append(x)
print(b)

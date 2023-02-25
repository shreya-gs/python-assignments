# greatest of three numbers

num = [10,15,20]

if (num[0] >= num[1]) and (num[0] >= num[2]):
    print(f"{num[0]} is greatest number.")    
elif (num[1]>=num[0]) and (num[1]>=num[2]):
    print(f"{num[1]} is greatest number.")    
else:
    print(f"{num[2]} is greatest number.")

# convert 0-9 digits only into word.

numbers = [0,1,2,3,4,5,6,7,8,9]
s = ''
for i in numbers:
    s += str(i)
    
print(s, type(s))
# WAP TO REVERSE THE WORDS

s = 'shreya'
# using string
rev = s[-1:-7:-1]
print(rev)

# using for loop
rev = ''
l = len(s)
for i in s:
    rev += s[l-1]
    l-=1
print(rev)    
    
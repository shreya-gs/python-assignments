# WAP TO ACCESS THE STRING USING SLICING AND INDEXING.

# using slicing 
s = "My name is Shreya."

# slicing method
a = s[3:7]
b = s[0:17:2]
c = s[-7:-1]
# d = s[-7:0] ==> empty string
# e = s[-1:-7] ==> empty string
f = s[-2:-7:-1]
print(a)
print(b)
print(c)
print(f)

s = "My name is Shreya."
# indexing method
i = 0
while i < (len(s)/2):
  print(s[i], end = '')
  
# to get single character
print(s[5])

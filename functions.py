# 1. Write a Python program to get a single string from two given strings, separated by a space,
# and swap the first two characters of each string
a=input()

b=input()

x=a[0:2]

a=a.replace(a[0:2],b[0:2])

b=b.replace(b[0:2],x)

print(a,b)

# 2.Write a Python function that takes a list of words and returns the longest word and the 
# length of the longest one
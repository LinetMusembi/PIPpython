# 1. Write a Python program to get a single string from two given strings, separated by a space,
# and swap the first two characters of each string

# a=input()
# b=input()
# x=a[0:2]
# a=a.replace(a[0:2],b[0:2])
# b=b.replace(b[0:2],x)
# print(a,b)

# 2.Write a Python function that takes a list of words and returns the longest word and the 
# length of the longest one

def find_longest_word(words):
    word_len = []
    for n in words:
        word_len.append((len(n),n))
    word_len.sort() 
    return word_len[-1][1]  
print(find_longest_word(["Lynet","Ann","Jemimah"]))


# 3. Write a Python program that accepts a comma-separated sequence of words as input and prints
# the distinct words in sorted form (alphanumerically).

fruits = ("mangoes","oranges","apples").split(",")
a = list(set(fruits))
a.sort()
print(str(a))


# 4.Write a Python function that takes two lists and returns True if they have at least one common member.
def check_common_member(list1,list2):
    result = False
    for x in list1:
     for y in list2:
            if x == y:
                result = True
    return result            
print(check_common_member([1,2,3],[4,9,7]))


# 5. Write a Python program to convert a list to a list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]

# color_name = ["Black","Red","Yellow"]
# color_code = ["#000000","#FF0000","#FFFF00"]
# print([{color_name:f,color_code:c}for f,c in zip(color_name,color_code)])

# 6.Write a Python program to check whether all dictionaries in a list are empty or not
l = [{},{},{}]
empty_list = True
for i in l:
    if i:
        empty_list=False
print(empty_list)        

# 7. Given a list of numbers, use list comprehension to remove all odd numbers from the list:
# numbers = [3,5,45,97,32,22,10,19,39,43]
nums=[3,5,45,97,32,22,10,19,39,43]
list1= [x for x in nums if x%2!=0]
print(list1)

# 8. Find the common numbers in two lists (without using a tuple or set) 
# list_a = 1, 2, 3, 4, 
# list_b = 2, 3, 4, 5
list1 = [1,2,3,4]
list2 = [2,3,4,5]
common = [a for a in list1 if a in list1]
print(common)

# 9. Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by 
# any single digit besides 1 (2-9)


# 10. Write a Python function to remove all vowels in a string
def remove_vowel(str):
    vowels = "a","e","i","o","u"
    result = [letter for letter in str if str.lower not in vowels]
    result = ",".join(result)
    print(result)



str = "lynet"
print(str)
remove_vowel(str)    
    
        
            
   
        


  
       

# 01 local vairable and global vairable
#Local Variables:

#1. Defined inside a function or block
#2. Accessible only within that function or block
#3. Exist only during function/block execution

#Global Variables:

#1. Defined outside functions or blocks
#2. Accessible from anywhere in the program
#3. Exist for the entire program duration
"""
x = 10  # Global
def my_function():
    y = 20  # Local
    print(x, y)
my_function()
print(x) """
#This code updates a global variable x from 10 to 77 using the global keyword inside a function.
"""
x = 10  # Global variable 'x' is initialized with value 10

def my_function():
    global x  # This tells Python that we are referring to the global variable 'x'
    x = 77    # The global variable 'x' is updated to 77

my_function()  # Call the function, which updates the global 'x'
print(x)       # Output the value of 'x' """

# 02 print sum of numbers using for loop
"""
user = int(input("enter your number:"))
total = 0
for i in range(1,user+1):
    print(i,end=" ")
    total += i
print()             ##This is just a blank print(), which tells Python:“Okay, now go to the next line.” other wise sum of total also prints in print(i,end = " ") thats only we use normal print()
print(f"sum of total:{total}")"""
#print sum of numbers using while loop
"""
user = int(input("enter your number:"))
total = 0
i = 1
while i <= user:
    print(i,end = " ")
    total += i
    i += 1
print()
print(f"sum of total:{total}")"""
# 03 write a program and print swap two vairable
"""
a = 7
b = 18
temp = a
a = b
b = temp
print(f"a = {a}")
print(f"b = {b}")"""
"""
a = 7
b = 18
a,b = b,a
print(f"a = {a}")
print(f"b = {b}")"""
# 04 print 17 table using for loop
"""
num = int(input("enter your number:"))
total = 0
for i in range(1,11):
    total = num * i
    print(f"{num} * {i} = {total}")"""
# print 17 table using while loop
"""
num = int(input("enter your number:"))
i = 1

while i <= 9:
     i+=1
     print(f"{num}x {i}={num*i}")"""
# 05 Generate Random number
# gives a random integer in specified range
"""
import random
num = random.randint(1,100)
print(num)"""

# gives a random float number between 0 and 1
"""
import random
num = random.random()
print(num)"""

# gives a random float number in specified number
"""
import random
num = random.uniform(1,100)
print(num)"""

# gives a random number in a range with incremental steps
"""
import random
num = random.randrange(0,100,2)
print(num)"""

# gives a sereis of random numbers
"""
import random
numlist = random.sample(range(0,100),3)
print(numlist)"""

# 06 print forward 5 stars patterns
"""
for i in range(1,6):
    print("* " * i)"""
"""
num = int(input("enter your number:"))
for i in range(1,num):
    print(" *" * i)"""

# 07 print reverse 5 stars patterns
"""
for i in range(5,0,-1):
    print(" *" * i)"""
"""num = int(input("enter your number:"))
for i in range(num,0,-1):
    print(" *" * i)"""

# 08 print forward pyramid type in 5 stars
"""
for i in range(1,6):
    spaces = " " *(5-i)
    stars = "* " * i
    print(spaces + stars)"""

# 09 print reverse pyramid type in 5 stars 
"""
for i in range(5,0,-1):
    spaces = " " * (5-i)
    stars = "* " * i
    print(spaces + stars)"""

# print 1 to 5 numbers like pattern only
"""
n = int(input("enter your number:"))
for x in range(1,n+1):
    for y in range(1,x+1):
        print(y,end =" ")
    print()"""

# print 5 to 1 numbers like pattern only
"""
num = int(input("enter your number:"))  # e.g., 5
for x in range(5, num-1 , -1):           # Starting from 5 down to 1
    for y in range(5, x-1 , -1):         # Print from 5 to x
        print(y, end=" ")
    print()"""


# 10 Write a Python program to print the first 10 natural numbers.
"""
for i in range(1,11):
    print(i)"""

# 11 Create a Python function to calculate the area of a rectangle.
"""
class rectangle:
    @staticmethod
  # def Box(self,len,wid):#if you didnot use self, u must and should give @staticmethod
    def Box(len,wid):
        return len * wid
per = rectangle()
print(per.Box(3,4))"""
"""
def rectangle(length,width):
    return (length * width)
print(rectangle(3,4))"""

# 12 Create a Python list and perform basic operations like append, insert, and delete.
"""
list =[0,1,2,3]
list.append(5)
list.remove(0)
list.insert(4,2)
list"""

# 13 Write a Python program to find the sum of all elements in a list.
"""
list = [1,2,34,4,5]
print(sum(list))"""

# 14 Create a Python dictionary and perform basic operations like insert, update, and delete.
"""
# Creating a dictionary
student = {
    "name": "Alice",
    "age": 20,
    "course": "Python"
}

# Insert a new key-value pair
student["grade"] = "A"
print("After Insert:", student)

# Update an existing value
student["age"] = 21
print("After Update:", student)

# Delete a key-value pair
del student["course"]
print("After Delete:", student)"""

# 15 Find common letters in two strings
"""
def common_letters():
    str1 = input("enter your string:")
    str2 = input("enter your string:")
    s1= set(str1)
    s2=set(str2)
    lst = s1 & s2
    print(lst)
    
common_letters()"""

# 16 write a python program to count the frequency of words appering in a string
"""
str = input("enter your sentence:")
words = str.split()
for word in words:
    print(word,"appears",words.count(word),"times")"""
"""
def freq_words():
    str = input("enter your string:")
    words = str.split()
    d = {}

    for word in words:
        if word not in d.keys():
            d[word] = 0
        d[word] = d[word]+1  #This line is increasing the count of a word in the dictionary d.
    print(d)
freq_words()"""

# 17 write a python program to convert two lists in to one dictionary
"""
keys = ["renu","chandu","jagathi","gopi","nani"]
values= [96,83,85,98,99]
d = dict(zip(keys,values))
print(d)"""

# 18 Remove duplicate characters in a string
"""
str = input("enter your string:")
str1 = set(str)
print(str1)"""

# 19 print armstrong numbers
"""
for i in range (1000,10000):
    s = i
    sum = 0
    while s > 0:
        d = s % 10
        sum = sum + d ** 4
        s = s // 10
        if i == sum:
            print("arm strong numbers",sum)"""

# 20 write a program and print Sort a list of tuples by the second element
"""
data = [(1,3),(2,1),(3,2)]
sorted_data = sorted(data,key=lambda x:x[1])
print(sorted_data)"""
for i in range(1,6):
    spaces = " " *(5-i)
    stars = " *" * i
    print(spaces + stars)


   

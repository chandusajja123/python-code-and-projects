# 01 write a programm and print leap year
"""
year = int(input("enter a year:"))
if (year % 4 == 0 and year % 100!= 0) or (year % 400 == 0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")"""

# 02 write a programm and print number of vowels and which vowels are been in your str
"""
str = input("enter a name:")
vowels = "aeiouAEIOU"
count = 0
found_vowels = ""
for char in str:
    if char in vowels:
        count += 1
        found_vowels += char
print(f"total {count} vowels in your str ")
print(f"this letters are found in your str '{found_vowels}',")"""
# 03 write a programm and print factorial programm using recursive function
"""
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))"""
#  write a programm and print factorial proramm using for loop
"""
n = int(input("enter a number:"))
product = 1
for i in range (1,n+1):
    product = product * i
print(f"factorial of {n} is {product}")"""
# 04 write a python program and print Remove duplicates from a list without using set().
a = [1,11,2,2,4,3,2,1,11,23,21,45,23]
unique_list = [] 
for item in a:
    if item not in unique_list:
        unique_list.append(item)
print("a:", a)
print("List after removing duplicates:", unique_list)

# 05 write a programm and print Reverse a string in Python
"""
str = input("enter your string:")
str1 = str[::-1]
print(str1)"""
# write a program Reverse a String without using in-built functions
"""
def reverse_string(s):
    result=""
    for char in s:
        result = char + result
    return result
print(reverse_string("sajja"))"""
# 06 write a programm and print Check if a string is a palindrome.
"""
str = input("enter your string:")
if str == str[::-1]:
    print(f"{str} is palindrome")
else:
    print(f"{str} is not palidrome")"""
# 07 write a programm and print Fibonacci series using (recursive)
"""
def fibonacci_recursive(n):
    
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
fibonacci_recursive(5)"""
# 08 write a programm and print number of vowels in given string
"""
str = input("enter your string:")
vowels = "aeiouAEIOU"
count = 0
for char in str:
    if char in vowels:
        count += 1
print(f"total number of vowels in your str {count} ")"""
# 09 calculator
"""
def addition(num1,num2):
    return num1 + num2
def subtraction(num1,num2):
    return num1 - num2
def multiplication(num1,num2):
    return num1 * num2
def division(num1,num2):
    if(num2==0):
        return "not divisible by 0!"
    return num1 / num2 
print("1.addition") 
print("2.subtraction") 
print("3.multiplication") 
print("4.divivsion") 
user = input("choose your  number(1/2/3/4):")
try:
   num1 = float(input("enter your first number:"))
   num2 = float(input("enter your second number:"))
   if user == "1":
      print(addition(num1,num2))
   
   elif user == "2":
      print(subtraction(num1,num2))
 
   elif user == "3":
      print(multiplication(num1,num2))
 
   elif user == "4":
      print(division(num1,num2))
   else:
      print("invalid numbers")
except  Exception as e:
     print("please enter only numbers")"""
# 10 todolist
"""
def addtask(todo_list):
    task=input("enter a task:")
    todo_list.append({"task":task,"status":"pending"})
    print(f"Task {task}  added to the to-do list.")
def viewtask(todo_list):
     if len(todo_list)==0:
          print("empty no tasks")
     else:
          for i,item in enumerate(todo_list,1):
               print(f"{i}:{item}")
def removetask(todo_list):
     if len(todo_list)==0:
          print("empty no tasks")
     else:
          i=int(input("enter item number"))
          if i<0 or i>len(todo_list):
               print("please enter correct item number!")
          else:
               print(f"removed item is:{todo_list.pop(i-1)}")
def marktask(todo_list):
      if len(todo_list)==0:
          print("empty no tasks")
      else:
          i=int(input("enter item number to mark as done:"))
          if i<0 or i>len(todo_list):
               print("please enter correct item number!")
          else:
               todo_list[i-1]["status"]="done"
               print(f"marked done of item is {todo_list[i-1]["status"]} has done")

def Todo_list():
    todo_list=[]
    while True:
            print("**TODO-LIST**\n")
            print("1.addtask") 
            print("2.viewtask") 
            print("3.removetask") 
            print("4.markdone") 
            print("5.exit") 
            user = input("enter your task(1/2/3/4/5):")
            if user=="1":
               addtask(todo_list)
            elif user=="2":
               viewtask(todo_list)
            elif user=="3":
               removetask(todo_list)
            elif user=="4":
               marktask(todo_list)
            elif user=="5":
                 print("exiting application...")
            else:
                 print("enter valid option fron 1-5")
Todo_list()"""
# 11 Anagram :- it means An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#Examples of Anagrams:
#"listen" → "silent"
#"eleven plus two" → "twelve plus one"
#"dormitory" → "dirty room"
# #Anagrams are often used in word games, puzzles, and cryptography for fun or mental challenges
"""
str1 = input("enter your string:")
str2 = input("enter your string:")
if sorted(str1) == sorted(str2):
    print("it is anagram")
else:
    print("it is not anagram")"""
"""
def anagram(str1,str2):
    return sorted (str1) == sorted(str2)
print(anagram("shannu","nnuash"))
print(anagram("chandu","gopi"))"""
# 12 fibonacci:-The Fibonacci sequence is a famous series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.
"""
def fibonacci(n):
    if n == 0:
       return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(6))"""
# 13 Two Sum Problem
#Given a list of numbers and a target number, return indices of the two numbers that add up to the target.
#Input: nums = [2, 7, 11, 15], target = 9 → Output: [0, 1]
#print(nums.index(2),nums.index(7))
"""
nums = [2, 7, 11, 15]
target = 9
num_map = {}

for i, num in enumerate(nums):
    complement = target - num
    if complement in num_map:
        print([num_map[complement], i])
        break
    num_map[num] = i"""
# 14 finiding average 
"""
str = input("enter your name:")
tel = int(input("enter your telugu marks:"))
eng = int(input("enter your english marks:"))
math = int(input("enter your maths marks:"))
scie = int(input("enter your science marks:"))
print("---------------------------------------")
print(f"Report of {str}")
print("----------------------------------------")
totalmarks = tel+eng + math+ scie
average = totalmarks/5
print(average)
print(f"your total msrks is {totalmarks}")
if totalmarks > 70:
    print(f"your marks is {totalmarks},your  grade is A")
else:
    print("your marks is {totalmarks},your  grade is B")
print("-------------------------------------------")"""
# 15 Bill calculation
"""
Bill = int(input("enter your total bills:"))
print("----------Bill Summary------------")
print(f"original Amount{Bill}:")
Discount = Bill * 80/100
Gst = Discount * 10/100
final_amount =  Discount + Gst
print(f"discount on product: {Discount}")
print(f"GST @ 10% on product:{Gst}")
print(f"final_amount :{final_amount}")"""
# Bill calculation program
"""
total_bill = float(input("Enter your total bill: ₹"))
discount = total_bill * 80/100  #0.80
gst = discount * 10/100         #0.10
final_amount = discount + gst

print("------Bill Summary------")
print(f"Original Amount: ₹{total_bill}")
print(f"Discount on product: ₹{discount}")
print(f"GST @ 10% on product: ₹{gst}")
print(f"Final amount: ₹{final_amount}")"""
# 16 prime number
"""
n= int(input("enter your number:"))
if n <= 1:
      print("it is not prime number")
else:
      for i in range(2,n):
          if n % i == 0:
                  print("it is not prime number")
                  break
      else:
          print("it is prime number")"""
# 17 prime number programm # see difference here else is not straight on if block
"""
n= int(input("enter your number:"))
for i in range(2,n):
    if n % i == 0:
            print("it is not prime number")
            break
else:
        print("it is prime number")"""
# count prime numbers from 1 to 100
"""
count = 0
prime_numbers = []
for num in range(1,101):
    if num < 2:
        continue
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        count += 1
        prime_numbers.append(num)
print(("Total prime numbers from 1 to 100:", count))
print("Prime numbers:", prime_numbers)"""
# 18 printing second largest number
"""
def secondlargest(nums):
    nums = list(set(nums))           #set(nums) → remove duplicates
                                     #list(set(nums)) → make it sortable,Because after removing duplicates, we want to 👉 And sort() only works on a list, not on a set.
    nums.sort()
    return nums[-2]

print(secondlargest([21,23,544,677,899,433,2,45,45,2,7]))"""

# 19 write a programm on  == and is
#== → checks value equality (do the objects have the same value?)
#is → checks identity (are they the same object in memory?)
"""
a = [1,2,3]
b = a
c = [1,2,3]

print(a == c)   # True (same content)
print(a is c)   # False (different memory)
                # True (same memory) 
print(a is b) """  
#20

#✅ 1. What is HCF/GCD? (Highest Common Factor)/(Greatest Common Divisior)
#🧠 Definition:
#HCF is the largest number that can divide both numbers without leaving a remainder.

#📌 Example:lets take 12 and 18
#Factors of 12 = 1, 2, 3, 4, 6, 12
#Factors of 18 = 1, 2, 3, 6, 9, 18
#Common factors = 1, 2, 3, 6
#👉 HCF = 6 (the biggest one)

#HCF(a,b) = HCF(b,a%b)

#✅ 2. What is LCM? (Least Common Multiple)
#🧠 Definition:
#LCM is the smallest number that is a multiple of both numbers.

#📌 Example: lets Take 12 and 18
#Multiples of 12 = 12, 24, 36, 48, ...
#Multiples of 18 = 18, 36, 54, ...
#👉 LCM = 36 (the smallest common one)

#LCM(a,b)= a * b/HCF(a,b)

"""
def HCF(a,b):
    if b != 0:
        return HCF(b,a%b)
    else:
        return a
print(HCF(12,18))"""
"""
def HCF(a, b):
    if b != 0:
        return HCF(b, a % b)
    else:
        return a
def LCM(a, b):
    hcf = HCF(a, b)
    lcm = (a * b) // hcf
    return lcm

print("LCM is:", LCM(12, 18))"""




#Right angle triangle
'''
def fun(n):
    for i in range(n):
       for j in range(i+1):
           print("*",end=" ")
       print()
n=int(input())   
fun(n)
'''


# Invert right angle
'''
def fun(n):
    for i in range(n):
      for j in range(n-i):
          print("*",end=" ")
      print()
n=int(input())  
fun(n)  '''















#equalateral triangle
'''
def fun(n):
    for i in range(n):
       for j in range(n-i-1):
           print(" ",end="")
       for j in range(i+1):
          print("*",end=" ")
       print()
n=int(input())
fun(n)
'''



#inevert equalateral
'''
def fun(n):
    for i in range(n):
      for j in range(i):
         print(" ",end="")
      for j in range(n-i):
         print("*",end=" ")
      print()
n=int(input())
fun(n)
'''



#reversw right angle
'''
def fun(n):
    for i in range(n):
       for j in range(n-i-1):
           print(" ",end=" ")
       for j in range(i+1):
           print("*",end=" ")    
       print() 
n=int(input())
fun(n)
'''




#diaomand pattern
'''
def fun(n):
    for i in range(n):
       for j in range(n-i-1):
           print(" ",end="")
       for j in range(i+1):
           print("*",end=" ")
       print()
    for i in range(n-1):
       for j in range(i+1):
           print(" ",end="")
       for j in range(n-i-1):
           print("*",end=" ")
       print()
n=int(input())
fun(n)
'''

'''
n=list(map(int,input().split()))
a=len(n)
i=0
j=0
k=6
while i<a:
    if n[i]==k:
        print("element found")
        j=1
    i+=1
             
if j==0:
    print("Element not found")
'''


#PYTHON CODES 
#Area of Rectangle
''' 
length=int(input())
width=int(input())
c=length*width
print("AREA OF RECTANGLE :", c )
'''
# user's name and age as input and prints a greeting message.
'''
name=input()
age=int(input())
print(f"Hello  {name} ! your {age} years old ")
'''
#check if a number is even or odd.
'''
num=int(input())
if num%2==0:
    print("Even number")
else:
    print("Odd number")
'''
#find the maximum and minimum values.
'''
a=list(map(int,input().split()))
maximum=max(a)
minimum=min(a)
print("Maximum number = ", maximum)
print("Minimum number = ", minimum)
'''
#check if a given string is a palindrome
'''
any=input()
if any==any[::-1]:
    print("palindrom")
else:
    print("not a palindrome")
'''
# Compound Interest Program
'''
P = float(input("Enter Principal Amount: "))
R = float(input("Enter Rate of Interest: "))
T = float(input("Enter Time Period (in years): "))

A = P * (1 + R/100) ** T
CI = A - P

print("Final Amount =", A)
print("Compound Interest =", CI)

'''
    

#Convert number of days into years, weeks, and days
'''

days = int(input("Enter number of days: "))

years = days // 365
remaining_days = days % 365

weeks = remaining_days // 7
days_left = remaining_days % 7

print("Years:", years)
print("Weeks:", weeks)
print("Days:", days_left)
'''



#Find the sum of all positive numbers in a list
'''
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

sum_positive = 0

for num in numbers:
    if num > 0:
        sum_positive += num

print("Sum of positive numbers:", sum_positive)
'''

#Count number of words in a sentence
'''
sentence = input("Enter a sentence: ")

words = sentence.split()
count = len(words)

print("Number of words:", count)
'''

#Swap the values of two variables

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)








  



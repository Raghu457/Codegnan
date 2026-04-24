'''
Handling Errors
------------------
try block
---------
-->The try block test the block of code for errors
Eg
---
try:
  print(b)

Except block
------------
-->This block will take care of any errors
else block
finally block
'''

'''
try:
    print(b)
except:
    print("This block can handle errors")
'''

'''
else block
---------
-->else keyword to define a block of code to be excuted if no error were raised
'''

'''
try:
    a=9
    b=10
    print(a+c)
except:
    print("Error here")
else:
    print("No error in the code")
'''

'''
finally block
--------------
--->This block will execute either try block have any error or no error
'''

'''
try:
    a=9
    b=10
    print(a+b)
except:
    print("Error here")
else:
    print("No error in the code")
finally:
    print("The try-except block is finished")
'''


try:
    num=int(input("Enter a number:"))
    num1=int(input("Enter a number:"))
    result=num/num1
    print(result+sum1)
except ValueError:
    print("Pls enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
except NameError:
    print("Pls enter valid name")
else:
    print(f"result: {result}")
finally:
    print("Program is completed")



    
    

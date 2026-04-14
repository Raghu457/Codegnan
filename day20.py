'''
Modules
-------
-->A module in a python is simply file that contain python code(Functions,Variable,classes)
-->To use modules, we have to use a keyword called import before the module
                                   Types of Modules
                                   ----------------
                            1.Built-in or Inbuilt     2.User-define modules

                            
'''

'''
#User defined modules
---------------------
-->This is developed by the user or programmer inside a file of python code and used by called import with filename...

Syntax--> import(keyword) file_name
           file_name.functionality

import mymodule
print(mymodule.add(4,7))
print(mymodule.sub(8,9))
'''


'''
Built-in or Inbuilt
-------------------
-->Already these are comes with installation and they are ready to use in the program
-->This is developed by the developer
Syntax-->import (keyword) module_name
         module_name.functionality
'''

'''
import math
print(math.sqrt(16))
'''

import random
k=random.randint(0,100)
print(k)
attempts=3
while attempts>0:
    n=int(input(f"Guess the number (you have {attempts} chances ):"))
    if k==n:
        print("True")
        break
    else:
        print("False")
    attempts-=1
if attempts==0:    
    l=input("You want to know what the random number is(Yes/No):")
    if l=="Yes":
        print(k)
    else:
        print("Game Over")



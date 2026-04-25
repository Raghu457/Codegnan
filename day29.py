'''
File handling
--------------
-->File handler is a n object of file to maintain several functions of file such as creating,reading,writing and update also deleting the file


How to open a file
------------------
1.open()
----------
-->This open() function takes 2 parameters and in this we have to close the file by calling close() function after program.
1.file name
2.mode

2.with open()
-------------


Modes  ("r","w","a","x","t")
-----
1."r"--read
----------
--->To read the file we use this mode and if the file doesn't exit. it will through the error
eg:
obj=open("demo.txt","r")
print(obj.read())
obj.close()


2."w"--write
-------------
-->To write the text into the file we will use this mode and it will create the file if it doesnt exist

obj=open("demo.txt","w")
obj.write("I am from visakhapatnam.")

obj.close()

'''


'''
3."a"--append
--------------
-->To add the text into the file this is used and it will create the file if it doesnt exist





obj=open("demo.txt","a")
obj.write("Andhra Pradesh.")
obj.close()

'''

'''
It automatically creates 
obj=open("some.txt","w")
obj.write("This is created file")
obj.close()
'''


'''
"x" -- "create"
-----------------
-->this is used to create the file,but is the file is already in the system it will raise error


'''

'''
To read a file
--------------
1.read()
--->This method can read the entire file chunk by chunk we can specify the size

2.readline()
--->This method can only read one line at a time

3.readlines()
-->This method can read the entire file and return into list with each line is one index in the list



eg:
obj=open("demo.txt","r")
print(obj.readlines())
obj.close
'''

import os
os.remove("some.txt")








































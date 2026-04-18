'''
Constructor (__init__)
---------------------
-->A constructor is a special method used to initialize object data
__init__()


class student:
    def __init__(self,name,ID):
        self.name = name
        self.ID = ID
    def display(self):
        print(self.name, self.ID)
Stu_1=student("Teja",123)
Stu_1.display()

'''



'''
Access Specifiers
-----------------
1.Public
Syntax-->name
we can use it any where in the program

2.Protected
Syntax -- _name
this is only for internal use

3.Private
Syntax--> __name
this one is restricted




class some:
    def __init__(self):
        self.public = "Public"
        self.protected="Protected"
        self.__private="Private"
any=some()
print(any.public)
print(any.protected)
print(any._some__private)


'''

'''
self
------
this keyword is instance variable and unique for different objects
'''




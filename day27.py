# Polymorphism
'''
--> Polymorphism means “many forms”.
--> In Object-Oriented Programming, polymorphism allows the same function/method name to behave differently depending on the object or data type.
--> Simply: One name, different behavior.

This allows a object of different classes to be treated as instance of the same base class , with methods behaving differently based on the actual object typeprint(
eg....
------
print(len("Python"))
print(len([1,2,3])
'''


'''
Method Overloading
------------------
-->This defines multiple methods with the same name but different parameters (number,type,or order) in the same class
'''

'''

class calculator:
    def add(self,a,b=0,c=0):
        return a+b+c
Cal=calculator()
print(Cal.add(2))
print(Cal.add(3,4))
print(Cal.add(5,7,8))
'''



'''
method Overriding
-----------------
--->This occurs in the child class,redefining a parent class method with the same signature for runtime.
'''

'''
class animal:
    def speak(self):
        return "Sound"

class dog(animal):
    def speak(self):
        return "Woof"
DOG=dog()
print(DOG.speak())
'''




'''
Operator Overloading
----------------------
-->This is customizes operator like +,- for user defined classes by implementing special methods ...
Eg...__add__,__sub__
'''

'''
class someone:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,other):
        return someone(self.a+other.a,self.b+other.b)
    def __str__(self):
        return f"{self.a},{self.b}"
any=someone(2,3)
so=someone(5,9)
print(any+so)
'''



'''
Data Abstraction
----------------
--->This hidex complex implementation details,exposing only essential features via abstract class or interface
'''
from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
Circle=circle(5)
print(Circle.area())































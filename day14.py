'''function()
-------------
--> This is a block of code which is reusable.
--> Two types 1.Built-in or In-build
              2.User define
1.Built-in or In-build
----------------------
-->They comes with program and those are already defined...
eg..
----> print(),sum(),map()......


2.User define
-------------
--> this is created by person who is developing or using for development


Note
----
--->it's starts with def keyword followed by func name
----> And it has calling function....


Syntax--> def func_name(a,b):  --->Parameters
             --------
             --------
             --------
          func_name(a,b)      --->Arguments
          
'''

'''
def add(a,b):
    c=a+b
    d=a-b
    e=a/b
    print("Sum:",c,"Sub:",d,"Div:",e)
a=int(input())
b=int(input())
add(a,b)
'''

'''
def add():
    if n%2==0:
        print("Even")
    else:
        print("ODD")
add()  '''


'''
def isprime(a):
    count=0
    for i in range(2,a+1):
        if a%i==0:
            count+=1
    if count==1:
        return True
    else:
        return False


a=int(input())
print(isprime(a))


#Palindrome number
def palin(a):
    rev=""
    for i in a:
        rev=i+rev
    if rev==a:
      print("Yes")
    else:
      print("No")
a=input()        
palin(a)        
'''









        
    
        
        






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















 equalateral triangle
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



















  



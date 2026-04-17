
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
    


















  



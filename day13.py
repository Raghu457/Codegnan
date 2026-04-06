
#Right angled triangle

'''
num=int(input())
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()    
'''

#square triangle
'''
num=int(input())
for i in range(1,num+1):
    for j in range(1,num+1):
        print("*",end=" ")
    print()'''



#reverse a triangle
'''
num=int(input())
for i in range(num+1):
    for j in range(num-i):
        print("*",end=" ")
    print()
'''

#equalateral triangle
'''
num=int(input())
for i in range(num):
    for j in range(num-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
     print()
    '''

'''
#alternate way
num=int(input())
for i in range(num):
    print(" "*(num-i),end="")
    for j in range(i+1):
        print("*",end=" ")
    print()    
'''



    

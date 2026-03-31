#Prime number
'''prime_num=int(input("Enter a number:"))
count=0
for i in range(1,prime_num):
    if prime_num%i==0:
        count+=1
if count==1:
    print("prime number")
else:
    print("Not a Prime number")'''


'''
prime=int(input("Enter a number"))

for j in range(1,prime+1):
    count=0
    for i in range(1,j+1):
        if j%i==0:
            count+=1
    if count==2:
        print(j,"is a prime number")

    else:
        print(j,"not a prime number")'''

'''
list_=[1057 ,197,9,86,17673]
for i in list_:
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(i,"is a prime number")
    else:
        print(i,"is not a prime number")'''


#remove duplicates
'''
any=[2,356,8,6,3,2,8]
arr=[]
for i in any:
    if i not in arr:
        arr.append(i)

 print(arr)    '''

#arm strong number
n=int(input())
length_ = len(str(n))
amstr_=0
for j in str(n):
    amstr_+=int(j)**length_
    print(amstr_)
if amstr_== n:
    print(f"{n} is Amstrong num")
else:
    print(f"{n} is not an Amstrong num")

        

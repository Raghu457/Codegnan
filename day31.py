'''
import re
def validate_name(name):
    pattern=r'^[A-Za-z]{3,.}$'
    return re.fullmatch(pattern,name)
def validate_email(email):
    pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.fulmatch(pattern,email)

def validate_phone(phone):
    pattern=r'^[0-9] {10}$'
    return re.fullmatch(pattern,phone)

def validate_password(password):
    pattern=r'^(?=.*[a-z]) (?=.*[A-Z]) (?=.*\d).{8,}$'
    return re.fullmatch(pattern,password)

def main():
    name=input("Enter Name:")
    email=input("Enter email:")
    phone=input("Enter Phone Number:")
    password=input("Enter Password:")


    if not validate_name(name):
        print("Invalid Name")
    elif not validate_email(email):
        print("Invalid Email")
    elif not validate_phone(phone):
        print("Invalid Phone")
    elif not validate_password(password):
        print("Invalid Password")
    else:
        print("All inputs are valid form submitted successfully")

if __name__ =="__main__":
    main()
'''


'''
Data Analysis
--------------
-->This is critical because it converts raw data into meaningful insights,enabling information to decision-making easy and improve operational efficiency...

1.Decion making
2.Improved Operational Efiiciency
3.Customer Understanding
4.Market Insight
5.Risk Management
6.Data_Driven Strategies


Line Plot
---------

import matplotlib.pyplot as pit
x=[200,40,60,80]
y=[1,2,3,4]
pit.plot(x,y)
pit.show()
'''


'''
Bar Graph
---------
import matplotlib.pyplot as pit
x=["Tv9","NDTV","SumanTV"]
y=[4,10,7]
pit.bar(x,y)
pit.show()
'''


'''
Pie Graph
---------
import matplotlib.pyplot as pit
x=[50,20,30]
y=['Dimple','Raghu','Tarun']
pit.pie(x,labels=y)
pit.show()

'''

'''
Histogram
---------
import matplotlib.pyplot as pit
pit.hist([23,15,78,12])
pit.show()
'''


'''
Numpy
------
-->Numpy(Numerical Python) is the foundational open-source library for scientific computing in python, providing high-performance, N-dimensional array objects (ndarray)
-->This enables efficient numerical computation linear algebra, and data manipulation,serving as the basis for tools like tensorflow and Scipy


pip install numpy



import numpy as np
arr=np.array([1,2,3,4])
print(arr)

'''



'''
Pandas
------
-->Pandas is used for handling structured data in table format


pip install pandas



'''

import pandas as pd
data={"Name":["Raghu","Dimple"],"Marks": [35,89]}
any=pd.DataFrame(data)
print(any)











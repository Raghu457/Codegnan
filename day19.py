'''
Generators
----------
-->This is a special type of function that return an ITERATOR which once at a time

yield
-----
--> It will take a pause and again resume,this is not a nrml keyword cannot be used in the nrml functions
--> This is used to produce a value and pause execution.

Next()
------
-->This is used to get next value from a generator
-->When the value is finished, it will stop the iterator

'''

'''
def my_generator():
    yield 1
    yield 2
    yield 3
an=my_generator()
print(next(an))
print(next(an))
print(next(an))
'''

'''
def square_gen(n):
    for i in range(n):
        yield i*i
for val in square_gen(5):
    print(val)
'''

'''

def square_gen(n):
    for i in range(n):
        yield i
        
for val in square_gen(100):
    print(val)
'''

ICIC_Raghu_AC_details={"Name":"Raghu","ATM PIN": "9100","Balance":5000,"Transaction History":[]}
print("Welcome to ICIC ATM")
print("Pls insert your ATM card")

ICIC_user_pin=input("Pls enter 4 digits ATM pin:")
if len(ICIC_user_pin)==4:
    
    if ICIC_user_pin in ICIC_Raghu_AC_details["ATM PIN"]:
        user_choice=int(input("Enter \n1.Withdraw:  \n2.Deposite: \n3.Pin change:  "))
        if user_choice==1:
            
            money_w=int(input("Enter money you want to withdraw"))
            if money_w<=ICIC_Raghu_AC_details["Balance"]:
                ICIC_Raghu_AC_details["Balance"] -= money_w
                print(ICIC_Raghu_AC_details["Balance"])
                
            else:
                print("insuff")
                
        elif user_choice==2:
            Deposite_m = int(input("plz enter the money you want to deposite: "))
            
            if Deposite_m % 100 == 0 and Deposite_m >=5000:
                ICIC_Raghu_AC_details["Balance"]+=Deposite_m
                ICIC_Raghu_AC_details["Transaction History"].append(f"Deposited: {Deposit_M}")
                print(f"[Deposited:{["Transaction History"]}]")
                
                print(f"you have depostied {Deposite_m} and the total ammount is {ICIC_Raghu_AC_details["Balance"]}")
            else:
                print(f"{Deposite_m} you have entered is change or less than given amount {5000}")
        elif user_choice ==3:
            old_pin=input("pls enter your old pin")

            if old_pin ==ICIC_Raghu_AC_details ["ATM PIN"]:
                new_pin=input("Enter new ATM PIN: ")
                
            if new_pin !=old_pin:
                ICIC_Raghu_AC_details ["ATM PIN"] = new_pin
                print("Your ATM pin updated succesfully")
                
            attempts_remaining==3
            while attempts_remaining > 0:
             old_pin = input("Enter your old ATM PIN: ")
             if len(old_pin)==4:
                if old_pin in user_choice["ATM PIN"]:
                   pin_change = input("Enter a new 4 digits ATM PIN: ")
                   user_choice["ATM PIN"]=pin_change
                   print("new pin is updated")
                
            else:
                print("you entered pin is incorrect")
            
        else:
            print("Enter correct number")
    else:
        print("You have entered invalid pin")
else:
    print("Plz enter 4 digit pin")





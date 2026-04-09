#Recursive function
'''
Recursion is a programming technique where function calls itself either directly or indirectly to solve a problem by breaking it into smaller , simpler subproblems .
Recursion is especially useful for problems that can be divided into identical smaller tasks, such as mathematical calculation , tree traversals or divide-and-conqure algorithms.'''


'''
def validate_pin(self):
    while self.remaining_attempts>0:
        user_pin = input("Enter 4 digit PIN:")
        if len(user_pin)==4 and user_pin == self.user_infoo["ATM PIN"]:
            print("Welcome to the ATM")
            return True
        else:
            self.remaining_attempts-=1
            if self.remaining_attempts>0:
                print(f"Invalid PIN. Attempts left: {self.remaining_attempts}")
            else:
                print("Card blocked. Please contact customer service")
                return False


'''

'''
def vo_con(n):
    c=[]
    c_1=[]
    for i in n:
        if i in "AEIOUaeiou":
            c.append(i)
        elif i==" " or i in "0123456789":
            pass
        else: 
            c_1.append(i)
    print(c)
    print(c_1)
n=input()    
vo_con(n)    
    '''


ICIC_Raghu_AC_details={"Name":"Raghu","ATM PIN": "9100","Balance":5000}
print("Welcome to ICIC ATM")
print("Pls insert your ATM card")
ICIC_user_pin=input("Pls enter 4 digits ATM pin:")
if len(ICIC_user_pin)==4:
    if ICIC_user_pin in ICIC_Raghu_AC_details["ATM PIN"]:
        user_choice=int(input("Enter \n1.Withdraw: \n2.Deposite:"))
        if user_choice==1:
            money_w=int(input("Enter money you want to withdraw"))
            if money_w<=ICIC_Raghu_AC_details["Balance"]:
                ICIC_Raghu_AC_details["Balance"] -= money_w
                print(ICIC_Raghu_AC_details["Balance"])
            else:
                print("insuff")
        elif user_choice==2:
            Deposite_M=int(input("Pls enter the money you want to deposite:"))
            if Deposite_M%100==0 and Deposite_M>=5000:
                ICIC_Raghu_AC_details['Balance']+=Deposite_M
                print(f"you have deposite {Deposite_M} and the total is {ICIC_Raghu_AC_details['Balance']}")
            else:
                print(f"{Deposite_M} you have entered is change or less than {5000}")
            
        else:
            print("Enter correct number")
    else:
        print("You have entered invalid pin")
else:
    print("Plz enter 4 digit pin")

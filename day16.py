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


def vo_con(n):
    c=[]
    c_1=[]
    for i in n:
        if i in "AEIOUaeiou":
            c.append(i)
        elif i==" " or i=="0123456789":
            pass
        
        else:
            c_1.append(i)
    print(c)
    print(c_1)
n=input()    
vo_con(n)    
    

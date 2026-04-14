
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

'''



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
        elif user_choice==4:
            transaction_amount=input("Enter the transaction amount")
            
            else:
                print("you entered pin is incorrect")
            print("Enter correct number")
    else:
        print("You have entered invalid pin")
else:
    print("Plz enter 4 digit pin")

'''





'''
append-->it adds a element at the end of the list

numbers = [1, 2, 3]
numbers.append(4)
print(numbers)

extend--> if adds multiple elements at the end of list
numbers = [1, 2]
numbers.extend([3, 4])
print(numbers)


insert--> it insert element according by there position
numbers = [1, 3, 4]
numbers.insert(1, 2)
print(numbers)


remove-->remove first occurence of specified value
numbers = [1, 2, 3]
numbers.remove(2)
print(numbers)

pop-->remove the element by there index value
numbers = [1, 2, 3]
numbers.pop()
print(numbers)


index-->it prints index value of specified value
numbers = [10, 20, 30]
print(numbers.index(20))


count-->if counts the number of occurences in the list
numbers = [1, 2, 2, 3]
print(numbers.count(2))

sort-->it return the numbers in acending order
numbers = [3, 1, 2]
numbers.sort()
print(numbers)


reverse-->It reverse entire list
numbers = [1, 2, 3]
numbers.reverse()
print(numbers)


copy-->it copy the given list
numbers = [1, 2, 3]
new_list = numbers.copy()
print(new_list)


clear-->It clear entire list
numbers = [1, 2, 3]
numbers.clear()
print(numbers)


#String methods
upper()-->It captilize all letters in the given string
text = "python"
print(text.upper())


lower()--->it return all letters in lower case
text = "PYTHON"
print(text.lower())

title()-->It captilize the first letters of the words
text = "python programming"
print(text.title())


captalize-->It captilize the first letter of entire string
text = "python"
print(text.capitalize())


strip()-->It remove white spaces of starting and ending of given string
text = "  python  "
print(text.strip())


replace-->It replace words according with the specified values
text = "I like Java"
print(text.replace("Java", "Python"))


split-->It splits the string into list with separator
text = "apple banana mango"
print(text.split())


join-->join list elements into string
words = ['Python', 'is', 'easy']
print(" ".join(words))


find-->It find there index value according to specified value
text = "python"
print(text.find("t"))

count-->count occurences of a substring
text = "banana"
print(text.count("a"))





'''


'''
a=input().lower()
b=input().lower()
if sorted(a)==sorted(b):
    print("Anagram")
else:
    print("Not a Anagram")

'''


n=int(input())
for 

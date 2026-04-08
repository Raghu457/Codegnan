

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

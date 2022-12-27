print("welcome to SBI bank")
pin = 2580
chances = 3
balance = 5000
while chances != 0:
    user_pin = int(input("please enter the four digit pin: "))
    if user_pin != pin:
        chances -= 1
        print("entered pin number is wrong")
        print(f"you have {chances} chances left")
    else:
        user_choice = input("B:balance,D:deposit,W:withdraw,E:exit: ")
        if user_choice == "B":
            print("                                                         ")
            print("                                                         ")
            print(f"your total balance is Rs. {balance}")
            if balance < 5000:
                print(f"""
                                            !!!!!WARNING...
                                            YOUR BALANCE IS LOW
                                            PLEASE CHECK IT
                                            """)
        if user_choice == "D":
            print("                                                         ")
            print("                                                         ")
            deposit_user = int(input("enter the amount that you want to deposit: "))
            total_balance = deposit_user + balance
            print(f"you have depositied rs.{deposit_user}")
            print(f"your total balance is Rs.{total_balance}")
            if total_balance < 5000:
                print(f"""
                                            !!!!!WARNING...
                                            YOUR BALANCE IS LOW
                                            PLEASE CHECK IT
                                            """)
        if user_choice == "W":
            print("                                                         ")
            print("                                                         ")
            withdraw_user = int(input("enter the amount that you want to withdraw: "))
            total_balance = balance - withdraw_user
            print(f"you have withdrwan Rs.{withdraw_user}")
            print(f"your total balance is Rs.{total_balance}")
            if total_balance < 5000:
                print(f"""
                                            !!!!!WARNING...
                                            YOUR BALANCE IS LOW
                                            PLEASE CHECK IT
                                            """)
        if user_choice == "E":
            print("                                                         ")
            print("                                                         ")
            print("WOULD YOU LIKE TO EXIT")
            user_choice = input("YES/NO")
            if user_choice == "YES":
                print("thanks for using SBI bank")

            if user_choice == "NO":
                print("""
                        PLEASE CONTINUE WITH NEW SESSION FOR SECURITY PURPOSE
                        """)
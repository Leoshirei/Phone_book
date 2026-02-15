#Phone Book

import os

choose = 0
while choose != 9:
    os.system("cls")
    print("--------------------")
    print("1. Add contact")
    print("2. Delete contact")
    print("3. Update contact")
    print("9. Save and Exit")
    print("--------------------")
    try:
        choose = int(input("Enter your choice: "))
        if choose == 1:
            print("You pressed 1")
        elif choose == 2:
            print("You pressed 2")
        elif choose == 3:
            print("You pressed 3")
        elif choose == 9:
            print("You pressed 9")
            exit()
        else:
            print("Wrong Choice!")
    except ValueError:
        print("Please enter a number!")
#Phone Book

import os
import logic
import person
import storage

choose = 0
phone_data = []
logic_phone = logic.Logic()
phone_data = storage.load_data()
while choose != 9:
    os.system("cls")
    print("--------------------")
    print("You have " + str(len(phone_data)) + " person in 'Phone Book'")
    print("1. Add contact")
    print("2. Delete contact")
    print("3. Update contact")
    print("4. Show all contacts")
    print("9. Save and Exit")
    print("--------------------")
    try:
        choose = int(input("Enter your choice: "))
        if choose == 1:
            person_phone = person.Person()
            logic_phone.add_contact(phone_data, person_phone)
        elif choose == 2:
            logic_phone.delete_contact(phone_data)
        elif choose == 3:
            if phone_data == []:
                print("You have no person in 'Phone Book'")
            else:
                logic_phone.update_contact(phone_data)
        elif choose == 4:
            if phone_data == []:
                print("You have no person in 'Phone Book'")
            else:
                logic_phone.show_contatcs(phone_data)
        elif choose == 9:
            storage.save_data(phone_data)
            exit()
        else:
            print("Wrong Choice!")
    except ValueError:
        print("Please enter a number!")
#Phone book
#Logic

import os

class Logic:
    def add_contact(self, person_list, person_object):
        os.system("cls")
        print("Adding person")
        print("--------------------")
        person_object.name = input("Enter name: ")
        while True:
            person_object.number = input("Enter phone number: ")
            if len(person_object.number) == 9:
                break
            else:
                print("Error phone number!")
        person_object.email = input("Enter email: ")
        person_list.append(person_object)

    def delete_contact(self, phone_list):
        os.system("cls")
        print("Deleteing person")
        print("--------------------")
        for index, person in enumerate(phone_list, start = 1):
            print(index, person.name, person.number, person.email)
        print("--------------------")
        try:
            in_delete = int(input("Wich person you want to delete: "))
            in_delete -= 1
            if in_delete < 0 or in_delete > len(phone_list):
                print("Error 404: person does not exist!")
            else:
                phone_list.pop(in_delete)
                print("Deleted person successfully!")
        except ValueError:
            print("Error 101: Wrong value")
    def show_contacs(self, phone_list):
        os.system("cls")
        for index, person in enumerate(phone_list, start = 1):
            print(index, person.name, person.number, person.email)
        os.system("pause")
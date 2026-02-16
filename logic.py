#Phone book
#Logic class

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
        print("Deleting person")
        print("--------------------")
        self._show_list(phone_list)
        print("--------------------")
        try:
            in_delete = int(input("Which person you want to delete: "))
            in_delete -= 1
            if in_delete < 0 or in_delete >= len(phone_list):
                print("Error 404: person does not exist!")
            else:
                phone_list.pop(in_delete)
                print("Deleted person successfully!")
        except ValueError:
            print("Error 101: Wrong value")

    def update_contact(self, phone_list):
        os.system("cls")
        print("Updating person data")
        print("--------------------")
        self._show_list(phone_list)
        print("--------------------")
        try:
            in_update = int(input("Which person you want to update: "))
            in_update -= 1
            if in_update < 0 or in_update >= len(phone_list):
                print("Error 404: person does not exist!")
            else:
                try:
                    os.system("cls")
                    print("Updating: " + phone_list[in_update].name, phone_list[in_update].number, phone_list[in_update].email)
                    print("1. Name")
                    print("2. Phone number")
                    print("3. Email")
                    person_choice = int(input("Which data you want to update: "))
                    if person_choice < 0 or person_choice > 3:
                        print("Error 403: data does not exist!")
                    elif person_choice == 1:
                        phone_list[in_update].name = input("Enter name: ")
                    elif person_choice == 2:
                        phone_list[in_update].number = input("Enter phone number: ")
                    elif person_choice == 3:
                        phone_list[in_update].email = input("Enter e-mail: ")
                except ValueError:
                    print("Error 101: Wrong value")
        except ValueError:
            print("Error 101: Wrong value")
            os.system("pause")

    def show_contatcs(self, phone_list):
        os.system("cls")
        self._show_list(phone_list)
        os.system("pause")

    def _show_list(self, phone_list):
        for index, person in enumerate(phone_list, start = 1):
            print(index, person.name, person.number, person.email)
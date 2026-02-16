#Phone book
#Logic

class Logic:
    def add_contact(self, person_list, person_object):
        person_object.name = input("Enter name: ")
        while True:
            person_object.number = input("Enter phone number: ")
            if len(person_object.number) == 9:
                break
            else:
                print("Error phone number!")
        person_object.email = input("Enter email: ")
        person_list.append(person_object)
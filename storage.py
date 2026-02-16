#Phone Book
#Storage functions

import json
import person

def save_data(phone_list):
    with open("Phone_book.json", "w") as file:
        person_to_dict = [persons.to_dict() for persons in phone_list]
        json.dump(person_to_dict, file, indent = 4)
def load_data():
    try:
        with open("Phone_book.json", "r") as file:
            person_to_dict = json.load(file)
            persons = []
            for person_data in person_to_dict:
                person_object = person.Person.from_dict(person_data)
                persons.append(person_object)
            return persons
    except FileNotFoundError:
        return []
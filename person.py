#Phone book
#Person class

import json

class Person:
    def __init__(self):
        self.name = None
        self.number = None
        self.email = None
    def to_dict(self):
        return {
            "name": self.name,
            "number": self.number,
            "email": self.email
        }
    @classmethod
    def from_dict(cls, data):
        person = cls()
        person.name = data["name"]
        person.number = data["number"]
        person.email = data["email"]
        return person

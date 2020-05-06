from abc import ABC, abstractclassmethod

class Person(ABC):
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @abstractclassmethod
    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}\nAge: {self.age}"

# TODO: think of what should be in Employee, Worker, Engineer

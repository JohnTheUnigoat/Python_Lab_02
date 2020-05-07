from abc import ABC, abstractclassmethod

# class Person(ABC):
class Person(ABC):
    def __init__(self, first_name, last_name, age, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}\nAge: {self.age}\nSalary: {self.salary}\n"


class Employee(Person):
    def __init__(self, first_name, last_name, age, salary, company_name):
        super().__init__(first_name, last_name, age, salary)
        self.company_name = company_name

    def __str__(self):
        res = super().__str__()
        res += f"Company: {self.company_name}\n"
        return res

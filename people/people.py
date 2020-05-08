from abc import ABC

class Person(ABC):
    def __init__(self, first_name, last_name, age, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.salary = salary

    @property
    def email(self):
        return f"{self.first_name.lower()}.{self.last_name.lower()}@mail.com"

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}\nAge: {self.age}\nEmail: {self.email}\nSalary: {self.salary}\n"


class Employee(Person):
    def __init__(self, first_name, last_name, age, salary, company_name):
        super().__init__(first_name, last_name, age, salary)
        self.company_name = company_name

    @property
    def email(self):
        return f"{self.first_name.lower()}.{self.last_name.lower()}@companyname.com"

    def __str__(self):
        res = "Employee:\n"
        res += super().__str__()
        res += f"Company: {self.company_name}\n"
        return res


class Worker(Person):
    def __init__(self, first_name, last_name, age, salary, job):
        super().__init__(first_name, last_name, age, salary)
        self.job = job

    def __str__(self):
        res = "Worker:\n"
        res += super().__str__()
        res += f"Job: {self.job}\n"
        return res


class Engineer(Person):
    def __init__(self, first_name, last_name, age, salary, speciality):
        super().__init__(first_name, last_name, age, salary)
        self.speciality = speciality

    @property
    def email(self):
        return f"{self.first_name.lower()}_{self.last_name.lower()}@mail.com"

    def __str__(self):
        res = "Engineer:\n"
        res += super().__str__()
        res += f"Speciality: {self.speciality}\n"
        return res

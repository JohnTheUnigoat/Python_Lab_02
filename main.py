from people import *
from random import randint

def generate_people(number):
    company_ctr = 1
    job_ctr = 1
    speciality_ctr = 1

    people = []

    for i in range(number):
        name = f"Name{i}"
        last_name = f"Lastname{i}"
        age = randint(20, 69)
        salary = randint(60, 1000) * 100

        switch = randint(0, 2)

        if switch == 0:
            people.append(
                Employee(
                    name,
                    last_name,
                    age,
                    salary,
                    f"Company {company_ctr}"
                )
            )
            company_ctr += 1
        elif switch == 1:
            people.append(
                Worker(
                    name,
                    last_name,
                    age,
                    salary,
                    f"Job {job_ctr}"
                )
            )
            job_ctr += 1
        elif switch == 2:
            people.append(
                Engineer(
                    name,
                    last_name,
                    age,
                    salary,
                    f"Speciality {speciality_ctr}"
                )
            )
            speciality_ctr += 1

    return people


def main():
    people = generate_people(20)

    for person in people:
        print(person)

    pass


if __name__ == '__main__':
    main()

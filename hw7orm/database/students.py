from faker import Faker
from db import session
from models import Student
from random import randint

fake = Faker()
NUMBER_GROUPS = 3

def create_students():
    for _ in range(30):
        student = Student(
            students_name = fake.name(),
            group_id = randint(1, NUMBER_GROUPS)
        )
        session.add(student)
    session.commit()


if __name__ == '__main__':
    create_students()
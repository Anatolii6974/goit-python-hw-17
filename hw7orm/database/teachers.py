from faker import Faker
from db import session
from models import Teacher

NUMBER_TEACHERS = 5

fake = Faker()

def create_teachers():
    for _ in range(NUMBER_TEACHERS):
        teacher = Teacher(
            teacher_name = fake.name()
        )
        session.add(teacher)
    session.commit()


if __name__ == '__main__':
    create_teachers()
from db import session
from models import Subject
from random import randint

NUMBER_TEACHERS = 5

# List of subjects
arr_subjects = ["Mathematics", "Physics", "History", "Chemistry", "Geography"]


def create_subjects():
    for s in arr_subjects:
        sub = Subject(
            subject = s,
            teacher_id = randint(1, NUMBER_TEACHERS)
        )
        session.add(sub)
    session.commit()


if __name__ == '__main__':
    create_subjects()
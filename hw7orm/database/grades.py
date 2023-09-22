from datetime import datetime
from db import session
from models import Grade
from random import randint

NUMBER_STUDENTS = 30
NUMBER_SUBJECTS = 5
NUMBER_GRADES = 20

def create_grades():
    for student in range(1, NUMBER_STUDENTS+1):
        for subject in range(1, NUMBER_SUBJECTS+1):
            for _ in range(4):
                grade = Grade(    
                    grade = (randint(1, 12)),
                    date = datetime(2023, randint(1, 5), randint(1, 28)).date(),       
                    student_id = student,
                    subject_id = subject
                )
                session.add(grade)
    session.commit()


if __name__ == '__main__':
    create_grades()
import sys
from sqlalchemy import func, desc, String
# from sqlalchemy.orm import joinedload
# from sqlalchemy import and_
# from datetime import datetime
from db import session
from models import Group, Student, Teacher, Subject, Grade

help_message = """
Виберіть який запит ви хочете виконати?
0 -- Вихід
1 -- Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
2 -- Знайти студента із найвищим середнім балом з певного предмета.
3 -- Знайти середній бал у групах з певного предмета.
4 -- Знайти середній бал на потоці (по всій таблиці оцінок).
5 -- Знайти, які курси читає певний викладач.
6 -- Знайти список студентів у певній групі.
7 -- Знайти оцінки студентів в окремій групі з певного предмета.
8 -- Знайти середній бал, який ставить певний викладач зі своїх предметів.
9 -- Знайти список курсів, які відвідує певний студент.
10 -- Список курсів, які певному студенту читає певний викладач.
"""


def select_1():
    students = (
    session.query(
        Student.students_name, 
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    )
    .select_from(Grade)
    .join(Student)
    .group_by(Student.id)
    .order_by(desc('avg_grade'))
    .limit(5)
    .all()
    )
    for s in students:
        print(s)


def select_2():
    students = (
    session.query(
        Student.students_name, 
        Subject.subject, 
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    )
    .select_from(Student)
    .join(Grade)
    .join(Subject, Subject.id == Grade.subject_id)
    .group_by(Student.id, Subject.id)
    .order_by(desc('avg_grade'))
    .limit(1)
    .all()
    )    
    for s in students:
        print(s)



def select_3():
    results = ( 
    session.query(
        Group.group_name,
        Subject.subject,
        func.round(func.avg(Grade.grade), 2).label('average_grade')
    )   
    .select_from(Student)
    .join(Group, Group.id == Student.group_id)
    .join(Grade,Grade.student_id == Student.id)
    .join(Subject, Subject.id == Grade.subject_id)
    .group_by(Group.id, Subject.subject)
    .all()
    )

    for result in results:
        group_name, subject, average_grade = result
        print(f"Group Name: {group_name}, Subject: {subject}, Average Grade: {average_grade}")


def select_4():
    result = (
        session.query(func.avg(Grade.grade).label('average_grade'))
        .scalar() 
    )

    print(f"Average Grade: {result:.2f}")


def select_5():
    results = (
        session.query(Teacher.teacher_name, func.string_agg(Subject.subject, ', ').label('subjects_taught'))
        .join(Subject, Subject.teacher_id == Teacher.id)
        .group_by(Teacher.teacher_name)
        .all()
    )

    for result in results:
        print(result.teacher_name, result.subjects_taught)


def select_6():
    results = (
        session.query(Group.group_name, func.string_agg(Student.students_name, ', ').label('ST_NAME'))
        .join(Student, Student.group_id == Group.id)
        .group_by(Group.group_name)
        .all()
    )

    for result in results:
        print(result.group_name, result.ST_NAME)


def select_7():
    results = (
        session.query(Group.group_name, Subject.subject, func.string_agg(Grade.grade.cast(String), ', ').label('GR'))
        .join(Student, Student.group_id == Group.id)
        .join(Grade, Student.id == Grade.student_id)
        .join(Subject, Grade.subject_id == Subject.id)
        .group_by(Group.group_name, Subject.subject)
        .all()
    )

    for result in results:
        print(result.group_name, result.subject, result.GR)


def select_8():
    result = (
        session.query(Teacher.teacher_name, Subject.subject, func.round(func.avg(Grade.grade), 2).label('average_grade'))
        .select_from(Grade)
        .join(Subject, Grade.subject_id == Subject.id)
        .join(Teacher, Teacher.id == Subject.teacher_id)
        .group_by(Teacher.teacher_name, Subject.subject)
        .all()
    )

    for row in result:
        print(f"Teacher: {row.teacher_name}, Subject: {row.subject}, Average Grade: {row.average_grade}")


def select_9():
    results = (
        session.query(Student.students_name, func.array_agg(func.distinct(Subject.subject)).label('subjects'))
        .select_from(Student)
        .join(Grade, Grade.student_id == Student.id)
        .join(Subject, Subject.id == Grade.subject_id)
        .group_by(Student.students_name)
        .all()
    )

    for result in results:
        print(f"Student: {result.students_name}, Subjects: {', '.join(result.subjects)}")


def select_10():
    results = (
        session.query(
            Student.students_name, Teacher.teacher_name, func.array_agg(func.distinct(Subject.subject)).label('subjects'))
            .select_from(Student)
            .join(Grade, Student.id == Grade.student_id)
            .join(Subject, Grade.subject_id == Subject.id)
            .join(Teacher, Subject.teacher_id == Teacher.id)
            .group_by(Student.students_name, Teacher.id)
            .all()
        )
    
    for result in results:
        print(f"Student: {result.students_name}, Techer: {result.teacher_name}, Subjects: {', '.join(result.subjects)}")



if __name__ == '__main__':
    print(help_message)
    while True:
        task = int(input("Виберіть номер запиту: "))
        if task == 0:
            sys.exit()
        match task:
            case 1:
                select_1()
            case 2:
                select_2()
            case 3:
                select_3()
            case 4:
                select_4()
            case 5:
                select_5()    
            case 6:
                select_6()  
            case 7:
                select_7()  
            case 8:
                select_8()  
            case 9:
                select_9()  
            case 10:
                select_10()             
            case _:
                print('Шо це таке?')
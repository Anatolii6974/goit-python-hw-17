from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime


Base = declarative_base()

# таблиця для зв'язку many-to-many між таблицями notes та tags

# Таблиця groups, де зберігатимуться назви груп
class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    group_name = Column(String(50), nullable=False)

# Таблиця students, де зберігатимуться записи про студентів
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    students_name = Column(String(255), nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship(Group, backref="students")

# Таблиця teachers, де зберігатимуться записи про викладачів
class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    teacher_name = Column(String(255), nullable=False)

# Таблиця tags, де зберігається набір предметів.
class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    subject = Column(String(255), nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    teacher = relationship(Teacher, backref="subjects")

    # Таблиця tags, де зберігається набір предметів.
class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    grade = Column(Integer)
    date = Column(DateTime, default=datetime.utcnow)
    student_id = Column(Integer, ForeignKey('students.id'))
    student = relationship(Student, backref="grades")
    subject_id = Column(Integer, ForeignKey('subjects.id'))
   

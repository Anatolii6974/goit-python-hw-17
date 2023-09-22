1. Docker контейнер:
docker run --name some-postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres
2. CREATE config.ini
3. CREATE database/db.py
4. CREATE database/models.py
5. poetry run alembic init alembic
6. EDIT alembic.ini 
7. EDIT alembic/env.py
8. poetry run alembic revision --autogenerate -m 'Init'
9. poetry run alembic upgrade head
-- seed --
10. poetry run py groups.py
11. poetry run py students.py
12. poetry run py teachers.py
13. poetry run py subjects.py
14. poetry run py grades.py

15. Для запитів файл my_select.py, де створені 10 функцій (select_1 - select_10)

poetry run py my_select.py

Вибрати який запит ви хочете виконати?
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





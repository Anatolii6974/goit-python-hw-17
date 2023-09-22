from db import session
from models import Group

# List of groups
arr_groups = ["A", "B", "C"]  

def create_groups():
    for g in arr_groups:
        group = Group(
            group_name = g
        )
        session.add(group)
    session.commit()


if __name__ == '__main__':
    create_groups()
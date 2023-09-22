"""Add teacher_id to Subject

Revision ID: 4312f4c5045e
Revises: b7202a8d0c2f
Create Date: 2023-09-17 16:08:45.141010

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4312f4c5045e'
down_revision: Union[str, None] = 'b7202a8d0c2f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subjects', sa.Column('teacher_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'subjects', 'teachers', ['teacher_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'subjects', type_='foreignkey')
    op.drop_column('subjects', 'teacher_id')
    # ### end Alembic commands ###

"""Change teacher_name

Revision ID: 8426ae869f11
Revises: 4312f4c5045e
Create Date: 2023-09-17 16:31:54.316683

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8426ae869f11'
down_revision: Union[str, None] = '4312f4c5045e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('teachers', sa.Column('teacher_name', sa.String(length=255), nullable=False))
    op.drop_column('teachers', 'students_name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('teachers', sa.Column('students_name', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    op.drop_column('teachers', 'teacher_name')
    # ### end Alembic commands ###

"""Add a column

Revision ID: b7202a8d0c2f
Revises: 97e3a3143bb0
Create Date: 2023-09-17 15:35:31.946824

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b7202a8d0c2f'
down_revision: Union[str, None] = '97e3a3143bb0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

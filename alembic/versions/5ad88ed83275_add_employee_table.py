'''add employee table

Revision ID: 5ad88ed83275
Revises: 22fd070aa8df
Create Date: 2023-11-08 14:02:32.458011

'''
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5ad88ed83275'
down_revision: Union[str, None] = '22fd070aa8df'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'employee',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String(50), nullable=False),
        sa.Column('last_name', sa.String(50), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('employee')

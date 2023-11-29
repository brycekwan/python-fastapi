'''create work order table

Revision ID: 10ee22a6129a
Revises: e26f2cd51d01
Create Date: 2023-11-08 14:59:02.277839

'''
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '10ee22a6129a'
down_revision: Union[str, None] = 'e26f2cd51d01'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'work_order',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('project_id', sa.Integer),
        sa.Column('employee_id', sa.Integer),
        sa.Column('rate', sa.Float)
    )


def downgrade() -> None:
    op.drop_table('work_order')

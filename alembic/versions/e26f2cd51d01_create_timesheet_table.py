'''create timesheet table

Revision ID: e26f2cd51d01
Revises: dda7319d708d
Create Date: 2023-11-08 14:58:52.291711

'''
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e26f2cd51d01'
down_revision: Union[str, None] = 'dda7319d708d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'timesheet',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('project_id', sa.Integer),
        sa.Column('work_order_id', sa.Integer),
        sa.Column('employee_id', sa.Integer),
        sa.Column('hours', sa.Float)
    )


def downgrade() -> None:
    op.drop_table('timesheet')

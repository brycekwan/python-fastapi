'''create project table

Revision ID: dda7319d708d
Revises: 3aeb892c60a0
Create Date: 2023-11-08 14:58:44.203788

'''
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dda7319d708d'
down_revision: Union[str, None] = '3aeb892c60a0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'project',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50))
    )


def downgrade() -> None:
    op.drop_table('project')

'''create invoice table

Revision ID: 3aeb892c60a0
Revises: 5ad88ed83275
Create Date: 2023-11-08 14:05:11.309701

'''
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3aeb892c60a0'
down_revision: Union[str, None] = '5ad88ed83275'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'invoice',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('customer_id', sa.Integer, nullable=False),
        sa.Column('hours', sa.Float),
        sa.Column('subtotal', sa.Float),
        sa.Column('total', sa.Float)
    )


def downgrade() -> None:
    op.drop_table('invoice')

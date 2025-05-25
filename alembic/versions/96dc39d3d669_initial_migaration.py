"""Initial migaration

Revision ID: 96dc39d3d669
Revises: 
Create Date: 2025-04-03 21:05:21.905078

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '96dc39d3d669'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('age', sa.int(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='py_khnu'
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users', schema='py_khnu')

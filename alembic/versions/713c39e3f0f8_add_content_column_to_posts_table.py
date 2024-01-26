"""add content column to posts table

Revision ID: 713c39e3f0f8
Revises: 69a4d0022e72
Create Date: 2024-01-25 16:53:24.333591

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '713c39e3f0f8'
down_revision: Union[str, None] = '69a4d0022e72'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass

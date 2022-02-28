"""Create blog table

Revision ID: 184bbedb561e
Revises: 
Create Date: 2022-02-28 19:33:00.158892

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic
revision = '184bbedb561e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'blog',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200))
    )


def downgrade() -> None:
    op.drop_table('blog')




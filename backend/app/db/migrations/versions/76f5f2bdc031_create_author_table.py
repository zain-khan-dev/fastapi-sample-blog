"""Create author table

Revision ID: 76f5f2bdc031
Revises: 184bbedb561e
Create Date: 2022-02-28 19:48:27.587260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic
revision = '76f5f2bdc031'
down_revision = '184bbedb561e'
branch_labels = None
depends_on = None


def upgrade() -> None:
        op.create_table(
        'author',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('email', sa.Unicode(200))
    )


def downgrade() -> None:
    op.drop_table('author')




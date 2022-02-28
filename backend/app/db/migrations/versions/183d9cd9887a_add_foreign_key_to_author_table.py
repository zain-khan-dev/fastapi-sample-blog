"""Add foreign key to author table

Revision ID: 183d9cd9887a
Revises: 76f5f2bdc031
Create Date: 2022-02-28 19:49:50.126991

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic
revision = '183d9cd9887a'
down_revision = '76f5f2bdc031'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_foreign_key(
            "fk_author_id", "blog",
            "author", ["author_id"], ["id"])


def downgrade() -> None:
    op.drop_constraint("fk_author_id", "blog")




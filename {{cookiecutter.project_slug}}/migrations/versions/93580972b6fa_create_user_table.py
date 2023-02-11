"""create user table

Revision ID: 93580972b6fa
Revises:
Create Date: 2023-02-11 18:53:27.738134

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "93580972b6fa"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("user_id", sa.Integer, primary_key=True),
        sa.Column("user_name", sa.String(50), nullable=False),
        sa.Column("comments", sa.Unicode(200)),
    )


def downgrade():
    op.drop_table("users")

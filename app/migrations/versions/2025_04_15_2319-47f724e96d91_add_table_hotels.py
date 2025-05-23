"""add table hotels

Revision ID: 47f724e96d91
Revises: ad7f7118a087
Create Date: 2025-04-15 23:19:40.685939

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "47f724e96d91"
down_revision: Union[str, None] = "ad7f7118a087"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "hotels",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("location", sa.String(length=100), nullable=False),
        sa.Column("services", sa.JSON(), nullable=True),
        sa.Column(
            "rooms_quantity", sa.Integer(), server_default=sa.text("0"), nullable=False
        ),
        sa.Column("image_id", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("hotels")
    # ### end Alembic commands ###

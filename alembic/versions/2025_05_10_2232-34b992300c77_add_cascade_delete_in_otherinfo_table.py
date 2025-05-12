"""add cascade delete in otherinfo table

Revision ID: 34b992300c77
Revises: 1a1a031805f2
Create Date: 2025-05-10 22:32:35.458821

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "34b992300c77"
down_revision: Union[str, None] = "1a1a031805f2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.drop_constraint(
        "fk_otherinfo_product_id_products", "otherinfo", type_="foreignkey"
    )
    op.create_foreign_key(
        op.f("fk_otherinfo_product_id_products"),
        "otherinfo",
        "products",
        ["product_id"],
        ["id"],
        ondelete="CASCADE",
    )
    op.alter_column(
        "products",
        "title",
        existing_type=sa.VARCHAR(length=255),
        type_=sa.String(length=300),
        existing_nullable=False,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        "products",
        "title",
        existing_type=sa.String(length=300),
        type_=sa.VARCHAR(length=255),
        existing_nullable=False,
    )
    op.drop_constraint(
        op.f("fk_otherinfo_product_id_products"),
        "otherinfo",
        type_="foreignkey",
    )
    op.create_foreign_key(
        "fk_otherinfo_product_id_products",
        "otherinfo",
        "products",
        ["product_id"],
        ["id"],
    )

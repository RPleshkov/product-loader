"""add product and otherinfo tables

Revision ID: 8286b724f917
Revises:
Create Date: 2025-05-10 21:13:58.962736

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "8286b724f917"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "products",
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("guid", sa.String(length=255), nullable=True),
        sa.Column("origin", sa.String(length=255), nullable=False),
        sa.Column("code", sa.String(length=255), nullable=False),
        sa.Column("origin_url", sa.String(length=255), nullable=False),
        sa.Column("preview_img", sa.String(length=255), nullable=False),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.Column("create_date", sa.DateTime(timezone=True), nullable=False),
        sa.Column("update_date", sa.DateTime(timezone=True), nullable=False),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_products")),
    )
    op.create_table(
        "otherinfo",
        sa.Column("product_id", sa.UUID(), nullable=False),
        sa.Column(
            "other_info",
            postgresql.JSONB(astext_type=sa.Text()),
            nullable=True,
        ),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["products.id"],
            name=op.f("fk_otherinfo_product_id_products"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_otherinfo")),
    )
    op.create_index(
        op.f("ix_otherinfo_product_id"),
        "otherinfo",
        ["product_id"],
        unique=False,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f("ix_otherinfo_product_id"), table_name="otherinfo")
    op.drop_table("otherinfo")
    op.drop_table("products")

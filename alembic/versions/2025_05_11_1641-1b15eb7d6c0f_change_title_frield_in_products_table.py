"""change title frield in products table

Revision ID: 1b15eb7d6c0f
Revises: 34b992300c77
Create Date: 2025-05-11 16:41:47.789828

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1b15eb7d6c0f"
down_revision: Union[str, None] = "34b992300c77"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        "products",
        "title",
        existing_type=sa.VARCHAR(length=300),
        type_=sa.String(length=350),
        existing_nullable=False,
    )



def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        "products",
        "title",
        existing_type=sa.String(length=350),
        type_=sa.VARCHAR(length=300),
        existing_nullable=False,
    )
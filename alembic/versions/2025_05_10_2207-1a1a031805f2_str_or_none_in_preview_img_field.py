"""str or None in preview_img field

Revision ID: 1a1a031805f2
Revises: 8286b724f917
Create Date: 2025-05-10 22:07:58.345692

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1a1a031805f2"
down_revision: Union[str, None] = "8286b724f917"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        "products",
        "preview_img",
        existing_type=sa.VARCHAR(length=255),
        nullable=True,
    )



def downgrade() -> None:
    """Downgrade schema."""

    op.alter_column(
        "products",
        "preview_img",
        existing_type=sa.VARCHAR(length=255),
        nullable=False,
    )


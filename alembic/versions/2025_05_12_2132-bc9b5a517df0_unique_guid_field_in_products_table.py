"""unique guid field in products table

Revision ID: bc9b5a517df0
Revises: 1b15eb7d6c0f
Create Date: 2025-05-12 21:32:46.081958

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "bc9b5a517df0"
down_revision: Union[str, None] = "1b15eb7d6c0f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_unique_constraint(op.f("uq_products_guid"), "products", ["guid"])



def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(op.f("uq_products_guid"), "products", type_="unique")


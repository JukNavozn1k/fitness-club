"""initial seed for roles and permissions

Revision ID: 2025_03_20_1200_seed
Revises: a390ee6645c1
Create Date: 2025-03-20 12:00:00.000000
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '2025_03_20_1200_seed'
down_revision = 'a390ee6645c1'
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Insert roles
    op.bulk_insert(
        sa.table(
            'roles',
            sa.column('id', sa.Integer),
            sa.column('name', sa.String)
        ),
        [
            {'id': 1, 'name': 'admin'},
            {'id': 2, 'name': 'trainer'},
            {'id': 3, 'name': 'member'},
        ]
    )
    # Insert permissions
    op.bulk_insert(
        sa.table(
            'permissions',
            sa.column('id', sa.Integer),
            sa.column('name', sa.String)
        ),
        [
            {'id': 1, 'name': 'create_workout'},
            {'id': 2, 'name': 'delete_workout'},
            {'id': 3, 'name': 'update_workout'},
            {'id': 4, 'name': 'view_workout'},
        ]
    )

def downgrade() -> None:
    # Remove seeded permissions
    op.execute("DELETE FROM permissions WHERE name IN ('create_workout', 'delete_workout', 'update_workout', 'view_workout')")
    # Remove seeded roles
    op.execute("DELETE FROM roles WHERE name IN ('admin', 'trainer', 'member')")
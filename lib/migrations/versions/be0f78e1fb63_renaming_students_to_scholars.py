"""Renaming students to scholars

Revision ID: be0f78e1fb63
Revises: 791279dd0760
Create Date: 2023-12-08 01:13:19.754993

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be0f78e1fb63'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')

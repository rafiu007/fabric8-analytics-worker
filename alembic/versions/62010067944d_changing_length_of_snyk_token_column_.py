"""Changing length of Snyk Token Column and datatype of user status.

Revision ID: 62010067944d
Revises: 661c60224dc8
Create Date: 2020-08-12 18:01:30.925730

"""

# revision identifiers, used by Alembic.
revision = '62010067944d'
down_revision = '661c60224dc8'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    """Upgrade the database to a newer revision."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user_details', 'snyk_api_token', existing_type=sa.VARCHAR(length=64),
                    type_=sa.String(length=255), existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    """Downgrade the database to an older revision."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user_details', 'snyk_api_token', existing_type=sa.String(length=255),
                    type_=sa.VARCHAR(length=64), existing_nullable=True)
    # ### end Alembic commands ###
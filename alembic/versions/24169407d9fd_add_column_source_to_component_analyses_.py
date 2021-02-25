"""add column source to component_analyses_request.

Revision ID: 24169407d9fd
Revises: 30d1b65971a2
Create Date: 2021-02-25 18:24:40.664498

"""

# revision identifiers, used by Alembic.
revision = '24169407d9fd'
down_revision = '30d1b65971a2'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    """Upgrade the database to a newer revision."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('component_analyses_requests',
                  sa.Column('source', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    """Downgrade the database to an older revision."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('component_analyses_requests', 'source')
    # ### end Alembic commands ###
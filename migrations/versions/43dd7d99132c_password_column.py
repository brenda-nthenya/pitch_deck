"""Password Column

Revision ID: 43dd7d99132c
Revises: c39d5bc5fdb2
Create Date: 2022-05-10 12:04:12.461730

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43dd7d99132c'
down_revision = 'c39d5bc5fdb2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###

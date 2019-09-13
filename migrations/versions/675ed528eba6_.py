"""empty message

Revision ID: 675ed528eba6
Revises: c2cee4505b47
Create Date: 2019-09-12 16:13:29.335901

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '675ed528eba6'
down_revision = 'c2cee4505b47'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=128), nullable=False),
    sa.Column('author', sa.String(length=84), nullable=False),
    sa.Column('description', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    # ### end Alembic commands ###

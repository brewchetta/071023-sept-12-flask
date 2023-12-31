"""empty message

Revision ID: f53607cb9e6e
Revises: 460a4ac35602
Create Date: 2023-09-12 16:35:59.738028

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f53607cb9e6e'
down_revision = '460a4ac35602'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('animals', schema=None) as batch_op:
        batch_op.drop_column('species')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('animals', schema=None) as batch_op:
        batch_op.add_column(sa.Column('species', sa.VARCHAR(), nullable=True))

    # ### end Alembic commands ###

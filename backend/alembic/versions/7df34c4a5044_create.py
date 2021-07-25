"""create

Revision ID: 7df34c4a5044
Revises: 
Create Date: 2021-05-28 13:14:25.038260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7df34c4a5044'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task_log', sa.Column('host', sa.String(length=50), nullable=True, comment='主机节点'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('task_log', 'host')
    # ### end Alembic commands ###
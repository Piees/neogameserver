"""empty message

Revision ID: 11725efb8271
Revises: 31140971ff88
Create Date: 2015-12-11 22:31:28.489827

"""

# revision identifiers, used by Alembic.
revision = '11725efb8271'
down_revision = '31140971ff88'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('host_server',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('servername', sa.String(), nullable=True),
    sa.Column('serverip', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('serverip'),
    sa.UniqueConstraint('servername')
    )
    op.create_table('port',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('portnumber', sa.Integer(), nullable=True),
    sa.Column('taken', sa.String(), nullable=True),
    sa.Column('hostserver', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['hostserver'], ['host_server.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column(u'order_product', sa.Column('mcport', sa.Integer(), nullable=True))
    op.add_column(u'order_product', sa.Column('ventport', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'order_product', 'port', ['mcport'], ['id'])
    op.create_foreign_key(None, 'order_product', 'port', ['ventport'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'order_product', type_='foreignkey')
    op.drop_constraint(None, 'order_product', type_='foreignkey')
    op.drop_column(u'order_product', 'ventport')
    op.drop_column(u'order_product', 'mcport')
    op.drop_table('port')
    op.drop_table('host_server')
    ### end Alembic commands ###

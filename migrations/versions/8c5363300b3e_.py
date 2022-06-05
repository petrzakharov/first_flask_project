"""empty message

Revision ID: 8c5363300b3e
Revises: e49ccbfd3ef7
Create Date: 2022-05-31 17:13:17.378180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c5363300b3e'
down_revision = 'e49ccbfd3ef7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'category', ['name'])
    op.create_unique_constraint(None, 'post', ['text'])
    op.create_unique_constraint(None, 'post', ['slug'])
    op.create_unique_constraint(None, 'post', ['title'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'post', type_='unique')
    op.drop_constraint(None, 'post', type_='unique')
    op.drop_constraint(None, 'post', type_='unique')
    op.drop_constraint(None, 'category', type_='unique')
    # ### end Alembic commands ###

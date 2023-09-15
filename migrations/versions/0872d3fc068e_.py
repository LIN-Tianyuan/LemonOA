"""empty message

Revision ID: 0872d3fc068e
Revises: 31b7214750ec
Create Date: 2023-05-20 23:50:03.797940

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0872d3fc068e'
down_revision = '31b7214750ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('email_captcha',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('captcha', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('email_captcha')
    # ### end Alembic commands ###

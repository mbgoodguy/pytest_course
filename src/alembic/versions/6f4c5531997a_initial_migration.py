"""initial migration

Revision ID: 6f4c5531997a
Revises: 
Create Date: 2024-04-06 20:42:43.462188

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f4c5531997a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('candies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.Column('state', sa.String(length=20), server_default='full', nullable=False),
    sa.Column('owner', sa.String(length=100), server_default='teacher', nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('candies')
    # ### end Alembic commands ###
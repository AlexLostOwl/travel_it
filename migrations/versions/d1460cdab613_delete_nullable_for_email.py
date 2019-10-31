"""delete_nullable_for_email

Revision ID: d1460cdab613
Revises: 4126df914610
Create Date: 2019-10-29 19:03:21.172559

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1460cdab613'
down_revision = '4126df914610'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
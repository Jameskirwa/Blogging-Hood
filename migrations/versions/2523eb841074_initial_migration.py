"""Initial Migration

Revision ID: 2523eb841074
Revises: 
Create Date: 2019-07-08 09:54:17.280948

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2523eb841074'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('bio', sa.String(length=1000), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('profile_pic_path', sa.String(), nullable=True),
    sa.Column('password_secure', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)
    op.create_table('blogs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('date_posted', sa.String(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_blogs_description'), 'blogs', ['description'], unique=False)
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=1000), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('blog_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['blog_id'], ['blogs.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    op.drop_index(op.f('ix_blogs_description'), table_name='blogs')
    op.drop_table('blogs')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_table('roles')
    # ### end Alembic commands ###

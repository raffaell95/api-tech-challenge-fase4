"""add colums uitem

Revision ID: 04c2fc6996e6
Revises: 8394196cdd87
Create Date: 2024-12-05 09:07:44.990347

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '04c2fc6996e6'
down_revision: Union[str, None] = '8394196cdd87'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('u_item', sa.Column('movie_id', sa.String(), nullable=True))
    op.add_column('u_item', sa.Column('movie_title', sa.String(), nullable=True))
    op.add_column('u_item', sa.Column('release_date', sa.String(), nullable=True))
    op.add_column('u_item', sa.Column('video_release_date', sa.String(), nullable=True))
    op.add_column('u_item', sa.Column('imdb_url', sa.String(), nullable=True))
    op.add_column('u_item', sa.Column('unknown', sa.String(), nullable=True))
    op.add_column('u_item', sa.Column('action', sa.String(), nullable=True))
    op.add_column('u_item', sa.Column('adventure', sa.String(), nullable=True))
    op.add_column('u_item', sa.Column('animation', sa.String(), nullable=True))
    op.add_column('u_item', sa.Column('childrens', sa.String(), nullable=True))
    op.add_column('u_item', sa.Column('comedy', sa.String(), nullable=True))
    op.add_column('u_item', sa.Column('crime', sa.String(), nullable=True))
    op.add_column('u_item', sa.Column('documentary', sa.String(), nullable=True))
    op.add_column('u_item', sa.Column('drama', sa.String(), nullable=True))
    op.add_column('u_item', sa.Column('fantasy', sa.String(), nullable=True))
    op.add_column('u_item', sa.Column('film_Noir', sa.String(), nullable=True))
    op.add_column('u_item', sa.Column('horror', sa.String(), nullable=True))
    op.add_column('u_item', sa.Column('musical', sa.String(), nullable=True))
    op.add_column('u_item', sa.Column('mystery', sa.String(), nullable=True))
    op.add_column('u_item', sa.Column('romance', sa.String(), nullable=True))
    op.add_column('u_item', sa.Column('sci_fi', sa.String(), nullable=True))
    op.add_column('u_item', sa.Column('thriller', sa.String(), nullable=True))
    op.add_column('u_item', sa.Column('war', sa.String(), nullable=True))
    op.add_column('u_item', sa.Column('western', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('u_item', 'western')
    op.drop_column('u_item', 'war')
    op.drop_column('u_item', 'thriller')
    op.drop_column('u_item', 'sci_fi')
    op.drop_column('u_item', 'romance')
    op.drop_column('u_item', 'mystery')
    op.drop_column('u_item', 'musical')
    op.drop_column('u_item', 'horror')
    op.drop_column('u_item', 'film_Noir')
    op.drop_column('u_item', 'fantasy')
    op.drop_column('u_item', 'drama')
    op.drop_column('u_item', 'documentary')
    op.drop_column('u_item', 'crime')
    op.drop_column('u_item', 'comedy')
    op.drop_column('u_item', 'childrens')
    op.drop_column('u_item', 'animation')
    op.drop_column('u_item', 'adventure')
    op.drop_column('u_item', 'action')
    op.drop_column('u_item', 'unknown')
    op.drop_column('u_item', 'imdb_url')
    op.drop_column('u_item', 'video_release_date')
    op.drop_column('u_item', 'release_date')
    op.drop_column('u_item', 'movie_title')
    op.drop_column('u_item', 'movie_id')
    # ### end Alembic commands ###

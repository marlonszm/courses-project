"""empty message

Revision ID: c55825792d6d
Revises: f35969e52992
Create Date: 2024-09-22 16:22:49.684033

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'c55825792d6d'
down_revision = 'f35969e52992'
branch_labels = None
depends_on = None

def upgrade():
    # Adicionar a chave estrangeira
    with op.batch_alter_table('curso', schema=None) as batch_op:
        batch_op.create_foreign_key('fk_curso_formacao', 'formacao', ['formacao_id'], ['id'])

def downgrade():
    # Remover a ForeignKey
    with op.batch_alter_table('curso', schema=None) as batch_op:
        batch_op.drop_constraint('fk_curso_formacao', type_='foreignkey')

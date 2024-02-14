"""created models

Revision ID: 09a1b2c8df50
Revises: 
Create Date: 2024-02-14 18:54:28.750426

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09a1b2c8df50'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('departments',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('department_name', sa.String(length=100), nullable=True),
    sa.Column('faculty_id', sa.String(length=36), nullable=True),
    sa.ForeignKeyConstraint(['faculty_id'], ['faculties.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('faculties',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('department_id', sa.String(length=36), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.id'], ),
    sa.ForeignKeyConstraint(['id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('semesters',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('start_date', sa.DATE(), nullable=True),
    sa.Column('end_date', sa.DATE(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('password', sa.String(length=50), nullable=True),
    sa.Column('role', sa.String(length=50), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('admin',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('courses',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('course_name', sa.String(), nullable=True),
    sa.Column('course_code', sa.String(), nullable=True),
    sa.Column('department_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lecturers',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('lecture_title', sa.String(), nullable=True),
    sa.Column('facult_id', sa.Integer(), nullable=True),
    sa.Column('datetime', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['facult_id'], ['faculties.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('students',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('department_id', sa.String(length=36), nullable=True),
    sa.Column('profile_photo', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('course_semester',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.Column('semester_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
    sa.ForeignKeyConstraint(['semester_id'], ['semesters.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('exams',
    sa.Column('unit_id', sa.String(length=36), nullable=False),
    sa.Column('score', sa.Float(), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('grade', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.PrimaryKeyConstraint('unit_id')
    )
    op.create_table('student_courses',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('units',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('unit_code', sa.String(length=36), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('passmark', sa.Float(), nullable=True),
    sa.Column('course_id', sa.String(length=36), nullable=True),
    sa.Column('contact_hours', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('course_work',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('unit_id', sa.Integer(), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('score', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.ForeignKeyConstraint(['unit_id'], ['units.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lecturer_unit',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('lecturer_id', sa.String(length=36), nullable=True),
    sa.Column('unit_id', sa.String(length=36), nullable=True),
    sa.ForeignKeyConstraint(['lecturer_id'], ['faculties.id'], ),
    sa.ForeignKeyConstraint(['unit_id'], ['units.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lecturer_unit')
    op.drop_table('course_work')
    op.drop_table('units')
    op.drop_table('student_courses')
    op.drop_table('exams')
    op.drop_table('course_semester')
    op.drop_table('students')
    op.drop_table('lecturers')
    op.drop_table('courses')
    op.drop_table('admin')
    op.drop_table('users')
    op.drop_table('semesters')
    op.drop_table('faculties')
    op.drop_table('departments')
    # ### end Alembic commands ###
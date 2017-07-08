from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
constraints = Table('constraints', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('constraint1_flt', Float(precision=20)),
    Column('constraint2_bool', Boolean),
    Column('constraint3_str', String(length=80)),
    Column('constraint4_sel', String(length=80)),
    Column('constraint5_selmult', String(length=80)),
    Column('constraint6_txtarea', String(length=200)),
    Column('constraint7_decimal', Float),
    Column('createddate', Float),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['constraints'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['constraints'].drop()

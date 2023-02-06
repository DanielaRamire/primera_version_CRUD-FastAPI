from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data

actor = Table("actor", meta_data,
Column("act_id", Integer, primary_key=True),
Column("act_fname", String(255), nullable=True),
Column("act_Iname", String(255), nullable=True),
Column("act_gender", String(255), nullable=True))

meta_data.create_all(engine)
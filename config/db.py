from sqlalchemy import create_engine. MetaData

engine = create_engine("mysql+pymysql://root:0000@localhost:3306/movie")

conn = engine.connect()

meta_data = MetaData()
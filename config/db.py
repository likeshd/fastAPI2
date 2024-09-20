from sqlalchemy import create_engine
from sqlalchemy import MetaData

engine = create_engine("mysql+pymysql://username:password@host:port/database")
meta =MetaData()

# Now you can use this 'users' table to insert data
conn = engine.connect()
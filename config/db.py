from sqlalchemy import create_engine
from sqlalchemy import MetaData

# engine = create_engine("mysql+pymysql://username:password@host:port/database")
engine = create_engine("mysql+pymysql://sql12732082:kY4wLQBiPL@sql12.freesqldatabase.com:3306/sql12732082")
meta =MetaData()

# Now you can use this 'users' table to insert data
conn = engine.connect()
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy

#from sqlalchemy_utils import database_exists, create_database
"""
#engine = create_engine("postgres://postgres@/postgres") 
engine = create_engine("postgresql://scott:tiger@localhost/mydatabase")

#create_engine("postgres://localhost/mydb")

if not database_exists(engine.url):
    create_database(engine.url)

print(database_exists(engine.url))
"""

 
# declare the connection string specifying
# the host name database name use name
# and password
conn_string = "host='localhost' dbname='try'\
user='root' password='pass'"


# Domain Host
#domain = ""
# use connect function to establish the connection
#engine = create_engine("mysql://scott:tiger@localhost/foo")
#engine = create_engine("sqlite:///foo.db")
#engine = create_engine("sqlite:///foo.db")
from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://user:password\
@hostname/database_name')

import psycopg2

# declare the connection string specifying
# the host name database name use name
# and password
conn_string = "host='localhost:5432)' dbname='dbData'\
user='root' password='pass'"

from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://scott:tiger@localhost:5432/mydatabase")


engine = create_engine("sqlite:///foo.db")
conn = engine.connect()

conn.execute("create TABLE food(name, price)")

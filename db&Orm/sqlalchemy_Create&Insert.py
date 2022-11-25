"""
https://vegibit.com/how-to-use-sqlalchemy-in-python/


https://builtin.com/data-science/python-sqlalchemy

https://docs.python.org/3/library/sqlite3.html

"""

import sqlalchemy as db


"""Connecting to engine -> ** Passing in the name of the 
	databse that we need to connect to.
	** Engine handles connection to multiple database.

"""
engine = db.create_engine('sqlite:///users.db')

## Create Database In SQLalchemy

metadata = db.MetaData()

connection = engine.connect()

data = "users"
users = db.Table(data, metadata,
                 db.Column('user_id', db.Integer, primary_key=True),
                 db.Column('first_name', db.Text),
                 db.Column('last_name', db.Text),
                 db.Column('email_address', db.Text))


posts = db.Table("posts", metadata,
	db.Column("id" , db.Integer, primary_key = True),
	db.Column("postContent", db.String),
	db.Column("tags", db.Text)
	)


metadata.create_all(engine)


""" Insert into tables ...
"""

UserRecords = users.insert().values([ 
	{"first_name": "Bob", "last_name": "Jones", "email_address": "bjones@notrealemail.com"},
    {"first_name": "Jack", "last_name": "Erich", "email_address": "jerich@notrealemail.com"},
    {"first_name": "Rick", "last_name": "Stein", "email_address": "rstein@notrealemail.com"},
    {"first_name": "Sally", "last_name": "Green", "email_address": "sgreen@notrealemail.com"}
])

postRecords = posts.insert().values([

	{"id" : 4 , "postContent" :"Vola this a random anonymous post ", "tags":"nan"},
	{"id" : 6 , "postContent" :"another dummy anonymous post", "tags":"nan"}


])

""" For avoiding multiple inserting with the same ids

connection.execute(postRecords)
connection.execute(UserRecords)

"""
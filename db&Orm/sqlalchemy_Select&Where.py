import sqlalchemy as db


"""To sum app steps of loading a table and display its recods
1- create engine `create_engine`
2- build a connection 
3- dump load the table
4- select the the res table -> works as a query that need to be executed
5- connection.execute -> store its val into a val AKA res 
6- fetch this res .
"""



engine = db.create_engine("sqlite:///users.db")

"""Load Table Into SQLAlchemy
"""
metadata = db.MetaData()

users = db.Table("users", metadata,autoload= True, autoload_with = engine)
print(users)

query = db.select([users])
print(query) ## it's not a result, it's just a query...


""" A query that needs to 1)- to forst excute and then, 2)- fetch

note that -> dnt forget to build a connection with the engine..

"""

connection = engine.connect()

res = connection.execute(query)
print(res)

print(res.fetchall())


""" $$ Adding Where clause 
"""
print()
print("$$ Adding Where clause ")
conditionalRecords = db.select([users]).where(users.columns.user_id == 1)

res = connection.execute(conditionalRecords)
print(res.fetchall())
print()
## To sum app steps of loading a table and display its 	recods
1- create engine _create_engine_

`engine = db.create_engine("sqlite:///users.db")
`

2- build a connection

`connection = engine.connect()
`

3- dump load the table

`users = db.Table("users", metadata,autoload= True, autoload_with = engine)
`

4- Select the the res table -> works as a query that need 
	to be executed 
	` query = db.select([users])`.

 - Using _where_ ,
  `conditionalRecords = db.select([users]).wher(users.columns.user_id == 1)`


5- connection.execute -> store its val into a val AKA res 
`res = connection.execute(conditionalRecords)`


6- fetch this res.`print(res.fetchall())`


**Code Snapshot**

```python
import sqlalchemy as db

engine = db.create_engine("sqlite:///users.db") 
metadata = db.MetaData()
connection = engine.connect()


users = db.Table("users", metadata,autoload= True, autoload_with = engine)

query = db.select([users])

res = connection.execute(query)

print(res.fetchall())

""" $$ Adding Where clause 
"""
print("$$ Adding Where clause ")
conditionalRecords = db.select([users]).where(users.columns.user_id == 1)

res = connection.execute(conditionalRecords)
print(res.fetchall())
```
## Create DataBase Table 


```python
data = "users"
users = db.Table(data, metadata,
                 db.Column('user_id', db.Integer, primary_key=True),
                 db.Column('first_name', db.Text),
                 db.Column('last_name', db.Text),
                 db.Column('email_address', db.Text))

```

## Inseting Bulk Data & Records

```python

UserRecords = users.insert().values([ 
	{"first_name": "Bob", "last_name": "Jones", "email_address": "bjones@notrealemail.com"},
    {"first_name": "Jack", "last_name": "Erich", "email_address": "jerich@notrealemail.com"},
    {"first_name": "Rick", "last_name": "Stein", "email_address": "rstein@notrealemail.com"},
    {"first_name": "Sally", "last_name": "Green", "email_address": "sgreen@notrealemail.com"}
])

postRecords = posts.insert().values([
	{"id" : 4 , "postContent" :"Vola this a random anonymous post ", "tags":"nan"},
	{"id" : 6 , "postContent" :"another dummy anonymous post", "tags":"nan"}])

connection.execute(postRecords)
connection.execute(UserRecords)

```
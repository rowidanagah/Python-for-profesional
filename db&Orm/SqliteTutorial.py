from sqlite3 import *

""" first we need to create a new database 
in the current working dir & path, so that we
 could work on it  or apply crud fuctionalites on..
"""
con = connect("tryDb.db")
"""while con is the representation of the connection to
	the ***on-disk database.
"""
#print(con)

cursor = con.cursor()
#print(cursor)

#cursor.execute("CREATE TABLE movie(title, year, score)")
cursor.execute("""
    INSERT INTO movie VALUES
    	('A Piace of your mind', 2019, 9.5),
        ('The Vow', 1975, 6.2),
        ('And Now for Something Completely Different', 1971, 7.5)
        ,('The ash', 1971, 7.5)
""")
res = cursor.execute("SELECT * FROM movie WHERE score > 9")
print(res.fetchall())
import sqlite3


db = sqlite3.connect('Login.db')
print("Connection Established")

cur = db.cursor()

cur.execute("DROP TABLE users") 

cur.execute("CREATE TABLE users(username TEXT,password TEXT)")

cur.execute("INSERT INTO users VALUES (?,?)",("harry","potter"))

print("First User Inserted in to users table")

cur.execute("INSERT INTO users VALUES (?,?)",("jon","snow"))

print("Second User Inserted in to users table")

db.commit()
print("Total {} Changes in the DB".format(db.total_changes))

db.close()

'''
How to read data from table
Execute below command:
    sqlite3 Login.db
Create new file i.e select script i.e. SelectUsers.sql
Execute below command:
    .read SelectUsers.sql

OR

select * from users;
'''
import sqlite3


db = sqlite3.connect('Login.db')
print("Connection Established")

cur = db.cursor()

cur.execute("DROP TABLE users")

cur.execute("CREATE TABLE users(username TEXT,password TEXT)")

cur.execute("INSERT INTO users VALUES (:user,:pass)", {"user":"harry","pass":"potter"})

print("First User Inserted in to users table")

cur.execute("INSERT INTO users VALUES (:user,:pass)", {"user":"jon","pass":"snow"})

print("Second User Inserted in to users table")

db.commit()

print("Total {} Changes in the DB".format(db.total_changes))

db.close()
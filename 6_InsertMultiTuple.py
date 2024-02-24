import sqlite3


db = sqlite3.connect('Login.db')
print("Connection Established")

Users = [("harry","potter"),

         ("tom","cat"),

         ("jon","snow")]

cur = db.cursor()

cur.execute("DROP TABLE users")

cur.execute("CREATE TABLE users(username TEXT,password TEXT)")

cur.executemany("INSERT INTO users VALUES (?,?)",Users)

print("Users Inserted in to users table")

db.commit()
print("Total {} Changes in the DB".format(db.total_changes))

db.close()
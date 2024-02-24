import sqlite3


def printDB(cursor):
   [print("{} : {}".format(row[0],row[1])) for row in cursor]


Users = [("harry","potter"),
       ("tom","cat"),
       ("jon","snow")]

db = sqlite3.connect('Login.db')
print("Connection Established")

cur = db.cursor()

cur.execute("DROP TABLE users")

cur.execute("CREATE TABLE users(username TEXT,password TEXT)")

cur.executemany("INSERT INTO users VALUES (?,?)",Users)

cur.execute("SELECT * FROM users")

printDB(cur)

cur.execute("DELETE FROM users WHERE username = ? ",("tom",))
print("The user tom has been deleted")

cur.execute("SELECT * FROM users")

printDB(cur)

db.commit()
print("Total {} Changes in the DB".format(db.total_changes))

db.close()
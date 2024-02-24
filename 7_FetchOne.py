import sqlite3


db = sqlite3.connect('Login.db')
print("Connection Established")

cur = db.cursor()

cur.execute("SELECT * FROM users ")

r1 = cur.fetchone()
r2 = cur.fetchone()
r3 = cur.fetchone()

print("{} : {}".format(r1[0],r1[1]))
print("{} : {}".format(r2[0],r2[1]))
print("{} : {}".format(r3[0],r3[1]))

print(type(r1))

db.commit()
print("Total {} Changes in the DB".format(db.total_changes))

db.close()
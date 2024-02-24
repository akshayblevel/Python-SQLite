import sqlite3


db = sqlite3.connect('Login.db')
print("Connection Established")

cur = db.cursor()

cur.execute("SELECT * FROM users")

for row in cur:
    print("{} : {}".format(row[0],row[1]))

cur.execute("UPDATE users SET password = ? WHERE username = ? ",("voldermort","harry"))
print("Updated password of  harry")

cur.execute("UPDATE users SET username = ? , password = ? WHERE username = ? ",("aegon","targaryen","jon"))
print("Updated username and password of jon")

cur.execute("SELECT * FROM users")

for row in cur:
    print("{} : {}".format(row[0],row[1]))

db.commit()
print("Total {} Changes in the DB".format(db.total_changes))

db.close()
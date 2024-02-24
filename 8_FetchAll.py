import sqlite3


db = sqlite3.connect('Login.db')
print("Connection Established")

cur = db.cursor()

cur.execute("SELECT * FROM users ")

allrows = cur.fetchall()

print(type(allrows))

for row in allrows:
    print("{} : {}".format(row[0],row[1]))


db.commit()
print("Total {} Changes in the DB".format(db.total_changes))

db.close()
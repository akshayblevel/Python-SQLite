import sqlite3


db = sqlite3.connect('Login.db')
print("Connection Established")

cur = db.cursor()

cur.execute("SELECT * FROM users ")

print(type(cur))

for row in cur:
    print("{} : {}".format(row[0],row[1]))

# Need to execute cur once again to get data
for row in cur:
    print("{} : {}".format(row[0],row[1]))

db.commit()
print("Total {} Changes in the DB".format(db.total_changes))

db.close()
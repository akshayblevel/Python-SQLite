import sqlite3

db = sqlite3.connect('Login.db')
print("Connection Established")

cur = db.cursor()
cur.execute("DROP TABLE users")

db.commit()
db.close()

'''
If table users is not available, you will get 
sqlite3.OperationalError: no such table: users
'''
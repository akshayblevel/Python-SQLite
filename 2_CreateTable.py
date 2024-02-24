# creating users table in Login.db with 2 columns username and password

import sqlite3

db = sqlite3.connect('Login.db')

print("Connection Established")

cur = db.cursor()
query = """
        CREATE TABLE IF NOT EXISTS
        users(username TEXT,password TEXT)
        """
cur.execute(query)

db.commit()
db.close()

'''
Verify the table creation using SQLite Command Line Shell
Execute command on terminal: sqlite3 Login.db
it will open sqlite command line i.e sqlite>
Execute: .tables
you can see -> users

.help will provide all commands
'''
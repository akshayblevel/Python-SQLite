import sqlite3

db = sqlite3.connect('Login.db')
print("Connection Established")
db.close()


'''
After you run .py a file named Login.db is created in the current directory
sqlite3.connect("Login.db") returns a connection object
If the db does not exist it will be created
'''
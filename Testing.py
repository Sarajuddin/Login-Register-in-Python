import sqlite3

def createTable():
    conn = sqlite3.connect('MyDatabase.db')
    cur = conn.cursor()
    cur.execute(f"CREATE TABLE IF NOT EXISTS Demo(name VARCHAR(50) NOT NULL, age INT, mobile VARCHAR(15), email VARCHAR(40) NOT NULL UNIQUE, password VARCHAR(50) NOT NULL, c_password VARCHAR(50) NOT NULL)")
    cur.close()

createTable()
print("Table is Created")

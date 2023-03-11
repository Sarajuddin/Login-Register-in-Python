import sqlite3

def createTable():
    conn = sqlite3.connect('MyDatabase.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Demo(name VARCHAR(50) NOT NULL, age INT, mobile VARCHAR(15), email VARCHAR(40) NOT NULL UNIQUE, password VARCHAR(50) NOT NULL, c_password VARCHAR(50) NOT NULL)")
    cur.close()
    conn.close()

def writeData(data_list):
    conn = sqlite3.connect('MyDatabase.db')
    cur = conn.cursor()
    insert_script = "INSERT INTO Demo(name, age, mobile, email, password, c_password) VALUES(?, ?, ?, ?, ?, ?)"
    insert_values = data_list
    cur.execute(insert_script, insert_values)
    cur.close()
    conn.close()

def getData(email, password):
    conn = sqlite3.connect('MyDatabase.db')
    cur = conn.cursor()
    select_script = "SELECT * FROM Demo WHERE email = ? AND password = ?"
    select_record = (email, password)
    cur.execute(select_script, select_record)
    
    data = cur.fetchall()

    cur.close()
    conn.close()
    return data
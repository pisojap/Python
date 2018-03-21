import sqlite3

databaseName = "books.db"
tableName = "book"

def connect():
    with sqlite3.connect(databaseName) as conn:
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS %s (id INTEGER PRIMARY KEY, Title TEXT, author TEXT, year INTEGER, isbn INTEGER)" % tableName)
        conn.commit()

def insert(title, author, year, isbn):
    with sqlite3.connect(databaseName) as conn:
        cur=conn.cursor()
        cur.execute("INSERT INTO " + tableName + " VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))            
        conn.commit()

def view():
    with sqlite3.connect(databaseName) as conn:
        cur=conn.cursor()
        cur.execute("SELECT * FROM %s" % tableName) 
        rows = cur.fetchall()           
        return rows        

connect()
#insert("The sea", "John Tablet", 1918, 9131123132)
#print(view())
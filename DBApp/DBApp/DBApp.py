import sqlite3

conn=sqlite3.connect("lite.db")
cur=conn.cursor()
conn.commit()
conn.close()

def createTable():
    with sqlite3.connect("lite.db") as conn:
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")

def insert(item, quantity, price):
    with sqlite3.connect("lite.db") as conn:
        cur=conn.cursor()
        cur.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price))

def view():
    with sqlite3.connect("lite.db") as conn:
        cur=conn.cursor()
        cur.execute("SELECT * FROM store")
        rows=cur.fetchall()
        return rows


createTable()
insert('Water', 10, 12.10)
print(view())
import sqlite3


def createTable():
    with sqlite3.connect("lite.db") as conn:
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
        conn.commit()

def insert(item, quantity, price):
    with sqlite3.connect("lite.db") as conn:
        cur=conn.cursor()
        cur.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price))
        conn.commit()

def view():
    with sqlite3.connect("lite.db") as conn:
        cur=conn.cursor()
        cur.execute("SELECT * FROM store")
        rows=cur.fetchall()
        return rows


createTable()
insert('Water', 10, 12.10)
print(view())
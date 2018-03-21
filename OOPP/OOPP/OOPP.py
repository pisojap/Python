import sqlite3

class Database:

    def __init__(self, db, table):
        self.db = db
        self.table = table
        self.conn = sqlite3.connect(self.db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS %s (id INTEGER PRIMARY KEY, Title TEXT, author TEXT, year INTEGER, isbn INTEGER)" % self.table)
        self.conn.commit()

    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO " + self.table + " VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))            
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM %s" % self.table) 
        rows = self.cur.fetchall()           
        return rows        

    def search(self, title = "", author = "", year = "", isbn = ""):
        self.cur.execute("SELECT * FROM " + self.table + " WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn)) 
        rows = self.cur.fetchall()           
        return rows        

    def delete(self, id):
        self.cur.execute("DELETE FROM " + self.table + " WHERE id=?", (id,))            
        self.conn.commit()

    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE " + self.table + " SET title=?, author=?, year=?, isbn=? WHERE id=?", (id, title, author, year, isbn, id))            
        self.conn.commit()

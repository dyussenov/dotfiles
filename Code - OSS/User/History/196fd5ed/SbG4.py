import sqlite3

conn = sqlite3.connect('orders.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   fname TEXT,
   lname TEXT,
   gender TEXT);
""")

conn.commit()
import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
   id INT PRIMARY KEY,
   name TEXT,
   surname TEXT,
   phone TEXT,
   password,
   email);
""")

conn.commit()
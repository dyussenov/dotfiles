import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
   id INT PRIMARY KEY,
   name TEXT,
   surname TEXT,
   phone TEXT,
   password TEXT,
   email TEXT);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS users(
   id INT PRIMARY KEY,
   customer_id INT,
   order_time TEXT,
   phone TEXT,
   password,
   email);
""")

conn.commit()
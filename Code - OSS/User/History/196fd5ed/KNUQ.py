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

cur.execute("""CREATE TABLE IF NOT EXISTS orders(
   id INT PRIMARY KEY,
   customer_id INT,
   order_time TEXT,
   delivery_address TEXT);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS orders_items(
   id INT PRIMARY KEY,
   order_id INT,
   item_id INT);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS items(
   id INT PRIMARY KEY,
   name TEXT,
   price INT,
   description TEXT);
""")

conn.commit()
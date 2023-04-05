import sqlite3

conn = sqlite3.connect('orders.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
   id INTEGER PRIMARY KEY,
   fname TEXT,
   lname TEXT,
   gender TEXT);
""")


more_users = [('Peter', 'Parker', 'Male'), ('Bruce', 'Wayne', 'male')]

#используем executemany()
cur.executemany("INSERT INTO users VALUES(?, ?, ?);", more_users)



conn.commit()
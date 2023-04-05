import sqlite3

conn = sqlite3.connect('knowledge-base.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS items(
   item_id TEXT PRIMARY KEY,
   value TEXT,
   parent_id TEXT);
""")
conn.commit()

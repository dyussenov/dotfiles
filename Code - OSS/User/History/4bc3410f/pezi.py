import sqlite3
from xml.dom import minidom


conn = sqlite3.connect('knowledge-base.db')
cur = conn.cursor()

file = minidom.parse('testfile.xml')
models = file.getElementsByTagName('mxCell')

cur.execute("""CREATE TABLE IF NOT EXISTS items(
   item_id TEXT PRIMARY KEY,
   value TEXT,
   parent_id TEXT);
""")
conn.commit()

for elem in models:
    try:
        value = elem.attributes['value'].value
        id = elem.attributes['id'].value
        cur.execute(f"""
        INSERT INTO items(item_id, value)
        VALUES('{id}', '{value}');
        """)
        conn.commit()
    except:
        pass

for elem in models:
    try:
        target = elem.attributes['target'].value
        source = elem.attributes['source'].value

        cur.execute(f"UPDATE items SET parent_id='{source}' where item_id='{target}';")
        conn.commit()
    except:
        pass
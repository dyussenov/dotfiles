import sqlite3

conn = sqlite3.connect('knowledge-base.db')
cur = conn.cursor()

cur.execute("SELECT * FROM items WHERE parent_id is null;")
root = cur.fetchone()
print(root[1])
current_item_id = root[0]
status = True
i = 0
while status:
    cur.execute(f"SELECT * FROM items WHERE parent_id = '{current_item_id}';")
    question = cur.fetchone()
    try:
        cur.execute(f"SELECT * FROM items WHERE parent_id = '{question[0]}';")
    except:
        print(question)
        break
    options = cur.fetchall()
    print(question)
    j = 0
    for o in options:
        print(f'{j}. {o[1]}')
        j+=1
    selected_option = int(input("выберите опцию: "))
    current_item_id = options[selected_option][0]

import sqlite3

connection = sqlite3.connect('database.db')
with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)", ('Перший пост', 'Привіт із подорожі!'))
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)", ('Другий пост', 'Тут дуже гарно.'))

connection.commit()
connection.close()
print("База даних готова!")
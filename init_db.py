import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

curr = connection.cursor()

curr.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
('First Post', 'Content for first post'))

curr.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
('Second Post', 'Content for second post'))

connection.commit()
connection.close()

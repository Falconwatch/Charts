import sqlite3

database_path = '../chartsite/db.sqlite3'

conn = sqlite3.connect(database_path)

cursor = conn.execute("select * from polls_COUNTS")

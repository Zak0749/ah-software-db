import sqlite3

conn = sqlite3.connect('database.db')

sql = "CREATE TABLE IF NOT EXISTS name (name varchar(16));"

conn.execute(sql)

cursor = conn.execute("SELECT name FROM name")
names = cursor.fetchall()

print("current names:")
for name in names:
  print(name[0])

new_name = input("would you like to add your name to the list if yes type it here:")

sql = "INSERT INTO name (name) VALUES ('" + new_name + "');"

conn.execute(sql)
conn.commit()
cursor = conn.execute("SELECT name FROM name")

names = cursor.fetchall()

print("all current names:")
for name in names:
  print(name[0])

conn.close()
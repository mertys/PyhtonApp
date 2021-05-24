import sqlite3

connection = sqlite3.connect('friend.db')
cursor = connection.cursor()
# cursor.execute("CREATE TABLE friends(first_name TEXT , last_name TEXT , age INTEGER)")
# cursor.execute("INSERT INTO friends VALUES ('Mert' , 'Yurtseven' , '29')")
# cursor.execute("SELECT * FROM friends WHERE first_name = 'Mahmut' ")

first_name = input('Adınız: ')
last_name = input('Soyadınız: ')
age = input('Yaşınız: ')

# cursor.execute(f"INSERT INTO friends  VALUES('{first_name}', '{last_name}' , {age})")

cursor.execute(f"INSERT INTO friends  VALUES(? , ? , ?)" , (first_name , last_name , age))


# print(cursor.fetchall())
connection.commit()
connection.close()

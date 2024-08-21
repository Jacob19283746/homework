import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

# for i in range(1, 11):
#     cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
#                    (f'User{i}', 'example{i}@gmail.com', i * 10, 1000))
# for i in range(1, 11, 2):
#     cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (500, i))
# for i in range(1, 11, 3):
#     cursor.execute('DELETE FROM Users WHERE username = ?', (f'User{i}',))
cursor.execute('SELECT username, email, age, balance  FROM Users WHERE age != 60')
res = cursor.fetchall()
# for i in res:
#     username, email, age, balance = i
#     print(f'Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}')

# cursor.execute('DELETE FROM Users WHERE username = ?', ('User6',))
cursor.execute('SELECT COUNT(*) FROM Users')
total = cursor.fetchone()[0]
cursor.execute('SELECT SUM(balance) from Users')
all_balance = cursor.fetchone()[0]
print(all_balance / total)
connection.commit()
connection.close()
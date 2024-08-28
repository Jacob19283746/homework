import sqlite3


def initiate_db():
    connection = sqlite3.connect('productbase.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Products
    (
    id INTEGER PRIMARY KEY
    AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    )
    ''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL, 
    age INT NOT NULL,
    balance INT NOT NULL
    )
    ''')
    cursor.execute('SELECT COUNT(*) FROM Products')
    count = cursor.fetchone()[0]
    if count == 0:
        product = [
            ('C-1000', 'Антиоксидантная защита', 1350),
            ('DMAE', 'Здоровая функция мозга', 1200),
            ('Biotin', 'Производство знергии', 1180),
            ('P-5-P', 'Здоровье нервнй системы', 1700)
        ]

        cursor.executemany('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', product)
    connection.commit()
    connection.close()


def add_user(username, email, age):
    connection = sqlite3.connect('productbase.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, 1000)', (username, email, age))
    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect('productbase.db')
    cursor = connection.cursor()
    cursor.execute('SELECT COUNT(*) FROM Users WHERE username = ?', (username,))
    result = cursor.fetchone()[0]
    connection.close()
    return result > 0


def get_all_products():
    connection = sqlite3.connect('productbase.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.close()
    return products


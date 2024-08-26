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


def get_all_products():
    connection = sqlite3.connect('productbase.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.close()
    return products


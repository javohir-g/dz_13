import sqlite3

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS clients (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT, phone TEXT, balance REAL);")

conn.commit()

def register_client(name, phone):
    try:
        cursor.execute("INSERT INTO clients (name, phone) VALUES (?, ?)", (name, phone))
        conn.commit()
        print(f"Клиент {name} успешно зарегистрирован!")
    except sqlite3.IntegrityError:
        print("Клиент с таким номером телефона уже существует.")

def find_client(name=None, phone=None):
    if name:
        cursor.execute("SELECT * FROM clients WHERE name = ?", (name,))
    elif phone:
        cursor.execute("SELECT * FROM clients WHERE phone = ?", (phone,))
    client = cursor.fetchone()
    return client

def deposit(phone, amount):
    cursor.execute("UPDATE clients SET balance = balance + ? WHERE phone = ?", (amount, phone))
    conn.commit()
    print(f"Баланс успешно пополнен на {amount} сум.")

def withdraw(phone, amount):
    cursor.execute("SELECT balance FROM clients WHERE phone = ?", (phone,))
    current_balance = cursor.fetchone()[0]
    if current_balance >= amount:
        cursor.execute("UPDATE clients SET balance = balance - ? WHERE phone = ?", (amount, phone))
        conn.commit()
        print(f"С вашего баланса было снято {amount} сум.")
    else:
        print("Недостаточно средств на балансе.")

def check_balance(phone):
    cursor.execute("SELECT balance FROM clients WHERE phone = ?", (phone,))
    balance = cursor.fetchone()[0]
    print(f"Ваш баланс: {balance} сум.")

def client_dashboard(phone):
    client = find_client(phone=phone)
    if client:
        print(f"Личный кабинет клиента {client[1]}")
        print(f"Телефон: {client[2]}")
        print(f"Баланс: {client[3]} сум")
    else:
        print("Клиент не найден.")

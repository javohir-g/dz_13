from database import *

while True:
    print("\nГлавное меню:"
            "\n1. Регистрация клиента"
            "\n2. Поиск клиента по телефону"
            "\n3. Пополнение баланса"
            "\n4. Снятие денег с баланса"
            "\n5. Просмотр баланса"
            "\n6. Личный кабинет клиента"
            "\n7. Выйти")

    choice = input("Выберите действие (1-7): ")

    if choice == "1":
        name = input("Введите имя клиента: ")
        phone = input("Введите телефон клиента: ")
        register_client(name, phone)
    elif choice == "2":
        phone = input("Введите телефон клиента: ")
        client = find_client(phone=phone)
        if client:
            print(f"Найден клиент: {client[1]}, Телефон: {client[2]}, Баланс: {client[3]}")
        else:
            print("Клиент не найден.")
    elif choice == "3":
        phone = input("Введите телефон клиента: ")
        amount = float(input("Введите сумму для пополнения: "))
        deposit(phone, amount)
    elif choice == "4":
        phone = input("Введите телефон клиента: ")
        amount = float(input("Введите сумму для снятия: "))
        withdraw(phone, amount)
    elif choice == "5":
        phone = input("Введите телефон клиента: ")
        check_balance(phone)
    elif choice == "6":
        phone = input("Введите телефон клиента: ")
        client_dashboard(phone)
    elif choice == "7":
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор, попробуйте снова.")

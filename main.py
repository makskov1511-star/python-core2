while True:
    print("\n--- МЕНЮ ---")
    print("1. Ввести число")
    print("2. Кількість цифр")
    print("3. Сума цифр")
    print("4. Середнє арифметичне")
    print("5. Кількість нулів")
    print("6. Вихід")

    choice = input("Оберіть пункт меню: ")

    if choice == "1":
        num = input("Введіть число: ")
        digits = num.lstrip("-")

    elif choice == "2":
        print("Кількість цифр:", len(digits))

    elif choice == "3":
        print("Сума цифр:", sum(int(x) for x in digits))

    elif choice == "4":
        total = sum(int(x) for x in digits)
        print("Середнє арифметичне:", total / len(digits))

    elif choice == "5":
        print("Кількість нулів:", digits.count("0"))

    elif choice == "6":
        print("Good bye!")
        break

    else:
        print("Неправильний вибір!")
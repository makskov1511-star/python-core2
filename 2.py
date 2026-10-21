score = int(input("Введіть бал за іспит (0-100): "))

if score < 0 or score > 100:
    print("Помилка! Значення поза діапазоном від 0 до 100.")
else:

    if 90 <= score <= 100:
        print("Відмінно")
    elif 70 <= score <= 89:
        print("Добре")
    elif 50 <= score <= 69:
        print("Задовільно")
    else:
        print("Незадовільно")

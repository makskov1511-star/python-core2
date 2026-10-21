month = int(input("Введіть номер місяця (1-12): "))

if month == 1 or month == 2 or month == 12:
    print("Winter")
elif 3 <= month <= 5:
    print("Spring")
elif 6 <= month <= 8:
    print("Summer")
elif 9 <= month <= 11:
    print("Autumn")
else:
    print("Помилка! Введене значення поза діапазоном від 1 до 12.")


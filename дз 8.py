n = int(input("Введіть розмір фігури: "))

print("Меню:")
print("1 - а")
print("2 - б")
print("3 - в")
print("4 - г")
print("5 - ж")
print("6 - з")
print("7 - и")
print("8 - к")
print("9 - д")
print("10 - е")

choice = int(input("Оберіть фігуру: "))

if choice == 1:  # а
    for i in range(n):
        print("*" * (n - i))

elif choice == 2:  # б
    for i in range(1, n + 1):
        print("*" * i)

elif choice == 3:  # в
    for i in range(n):
        print("*" * (n - i) + " " * i)

elif choice == 4:  # г
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)

elif choice == 5:  # ж
    for i in range(n):
        print("*" * (i + 1) + " " * (n - i - 1))

elif choice == 6:  # з
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (i + 1))

elif choice == 7:  # и
    for i in range(n):
        print("*" * (n - i) + " " * i)

elif choice == 8:  # к
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)

elif choice == 9:  # д
    for i in range(n):
        print("*" * (i + 1) + " " * (2 * (n - i - 1)) + "*" * (i + 1))
    for i in range(n - 1, -1, -1):
        print("*" * (i + 1) + " " * (2 * (n - i - 1)) + "*" * (i + 1))

elif choice == 10:  # е
    for i in range(n):
        print("*" * (i + 1) + " " * (2 * (n - i - 1)) + "*" * (i + 1))
    for i in range(n - 1, -1, -1):
        print("*" * (i + 1) + " " * (2 * (n - i - 1)) + "*" * (i + 1))

else:
    print("Такого пункту меню немає.")
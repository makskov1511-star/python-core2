def sum_range(a, b):
    if a > b:
        a, b = b, a

    summa = 0

    for i in range(a, b + 1):
        summa += i

    return summa


a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))

print("Сума:", sum_range(a, b))
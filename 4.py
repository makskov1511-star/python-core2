number_str = input("Введіть будь-яке ціле число: ")

digit_sum = 0
for char in number_str:
    if char.isdigit():
        digit_sum += int(char)

if digit_sum % 2 == 0:
    print("Сума цифр парна")
else:
    print("Сума цифр непарна")

user_input = input("Введіть ціле шестизначне число: ")

if len(user_input) == 6 and user_input.isdigit():
    digits = list(user_input)

    digits[0], digits[5] = digits[5], digits[0]

    digits[1], digits[4] = digits[4], digits[1]

    result = "".join(digits)
    print(f"Результат: {result}")
else:
    print("Помилка: введене число не є шестизначним!")

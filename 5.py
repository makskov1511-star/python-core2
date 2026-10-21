user_input = input("Введіть ціле шестизначне число: ")

if len(user_input) == 6 and user_input.isdigit():
    first_half = [int(d) for d in user_input[:3]]
    second_half = [int(d) for d in user_input[3:]]

    if sum(first_half) == sum(second_half):
        print("Число є щасливим")
    else:
        print("Число не є щасливим")
else:
    print("Помилка: введене число не є шестизначним!")

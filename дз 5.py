
number = int(input("Введіть число від 1 до 100: "))

if number < 1 or number > 100:
    print("Помилка! Число має бути від 1 до 100.")
elif number % 3 == 0 and number % 5 == 0:
    print("Fizz Buzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)

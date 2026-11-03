while True:
    num = int(input("Введіть число: "))

    if num == 7:
        print("Good bye!")
        break
    elif num > 0:
        print("Number is positive")
    elif num < 0:
        print("Number is negative")
    else:
        print("Number is equal to zero")
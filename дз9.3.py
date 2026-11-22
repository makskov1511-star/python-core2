def square(n, symbol, filled):
    for i in range(n):
        if filled:
            print(symbol * n)
        else:
            if i == 0 or i == n - 1:
                print(symbol * n)
            else:
                print(symbol + " " * (n - 2) + symbol)


n = int(input("Введіть довжину сторони: "))
symbol = input("Введіть символ: ")
filled = bool(int(input("Заповнений? (1 - так, 0 - ні): ")))

square(n, symbol, filled)
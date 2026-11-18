def add(a, b):
    return a + b


def dif(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


def f(n):
    if n == 0:
        return 1
    else:
        return n * f(n - 1)
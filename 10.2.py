def multiply_list(numbers):
    result = 1

    for i in numbers:
        result *= i

    return result


numbers = [2, 3, 4, 5]

print("Добуток:", multiply_list(numbers))
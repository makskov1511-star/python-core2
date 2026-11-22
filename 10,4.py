def power_list(numbers, power):
    result = []

    for i in numbers:
        result.append(i ** power)

    return result


numbers = [2, 3, 4]
power = 2

print(power_list(numbers, power))
def sort_numbers(numbers):
    even_numbers = []
    odd_numbers = []
    positive_numbers = []
    negative_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

        if num > 0:
            positive_numbers.append(num)
        else:
            negative_numbers.append(num)

    return even_numbers, odd_numbers, positive_numbers, negative_numbers


numbers = [-5, -4, -1, 0, 2, 3, 6, 9]

even, odd, positive, negative = sort_numbers(numbers)

print("Парні числа:", even)
print("Непарні числа:", odd)
print("Позитивні числа:", positive)
print("Негативні числа:", negative)
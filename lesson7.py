size = int(input("Введіть розмір клітинки: "))

for i in range(8 * size):
    for j in range(8 * size):
        if (i // size + j // size) % 2 == 0:
            print("#", end="")
        else:
            print(" ", end="")
    print()
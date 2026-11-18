def product(a: int, b: int):
    if a > b:
        a, b = b, a
    i = 1
    for i in range(a,b+1):
        i += 1

    return i

print(product(1,5))



def max_of_list(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i

    return max

print(max_of_list([10,11,7,9]))




def sum_and_avg(list):
    i = 0
    for a in list:
        i+=a
        avg = i/len(list)
    return i,avg

print(sum_and_avg([1,2,3,4]))




def pos_neg_even_odd(list):
    i = 0
    for i in list:
        if i % 2 == 0:
            print(f"{i} is even")
        if i % 2 == 1:
            print(f"{i} is odd")
        if i < 0:
            print(f"{i} is negative")
        if i > 0:
            print(f"{i} is positive")

print(pos_neg_even_odd([4,8,0,-7]))
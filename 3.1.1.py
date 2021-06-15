def func(list):
    result = 1
    for i in list:
        result *= i
    return result

l = [8, 2, 3, -1, 7]
print(func(l))

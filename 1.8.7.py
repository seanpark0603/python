a = [1, 2, 3, 2, 4, 5, 1, 5]
b = [1, 5, 7, 2]
common = []
for x in a:
    if x not in common and x in b:
        common.append(x)
print(common)

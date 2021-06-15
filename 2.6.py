import timeit

f = open("C:/Users/seanp/Documents/성준/coding/python_hw04.txt", "rt")
start = timeit.default_timer()

sum = 0

i = 0
while i < 10:
    d = {}
    f = open("C:/Users/seanp/Documents/성준/coding/python_hw04.txt", "rt")
    start = timeit.default_timer()
    while True:
        line = f.readline()[0:-1]
        if not line: break
        d[line] = 0

    f.close()
    stop = timeit.default_timer()
    sum += stop-start
    i += 1
print(sum/10)
sum = 0
i = 0

while i < 10:
    l = []
    f = open("C:/Users/seanp/Documents/성준/coding/python_hw04.txt", "rt")
    start = timeit.default_timer()
    while True:
        line = f.readline()[0:-1]
        if not line: break
        l.append(line)

    f.close()
    stop = timeit.default_timer()
    sum += stop-start
    i += 1
print(sum/10)

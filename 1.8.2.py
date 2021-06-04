thislist = ['abc', 'xyz', 'aba', '1221']
cnt = 0
for x in thislist:
    if len(x) >= 2:
        if x[0] == x[-1]:
            cnt = cnt+1
print(cnt)

n = int(input())
ls = []
for i in range(n):
    act = tuple(map(int, input().split()))
    ls.append(act)

ls.sort(key=lambda a: a[1])

count, end = 1, ls[0][1]
for i in range(1, n):
    if ls[i][0] >= end:
        count += 1
        end = ls[i][1]
        print(ls[i])

print(count)
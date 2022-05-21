n = 10
a = []
# 上边界一排0
a.append([0] * 12)
# 左右各 + 0
for i in range(n):
    a.append([0] + list(int(x) for x in input().split()) + [0])
# 下边界一排0
a.append([0] * 12)

grid = []
grid.append([0, 0])
while len(grid) > 0:
    p = grid.pop(0)
    x = p[0]
    y = p[1]
    if y < 0 or y >= n + 2: continue
    if x < 0 or x >= n + 2: continue
    if a[y][x] == 1: continue
    if a[y][x] == 2: continue
    a[y][x] = 2
    grid.append([x + 1, y])
    grid.append([x - 1, y])
    grid.append([x, y - 1])
    grid.append([x, y + 1])

ret = 0
for i in range(12):
    ret += a[i].count(0)
print(ret)
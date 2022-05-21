class MyQueue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


ls = list(map(int, input().split()))
n = ls[0]
ls.remove(ls[0])
a = MyQueue()
b = MyQueue()
res = []
j = 0
for i in ls:
    if i % 2 == 0:
        b.push(i)
    else:
        a.push(i)
for i in range(1, len(ls) + 1):
    if a.size() > 0:
        res.append(a.pop())
        j += 1
    if b.size() > 0 and j % 2 == 0:
        res.append(b.pop())
        j = 0
s = len(res)
for i in range(n):
    if i == n - 1:
        print(res[i], end="")
    else:
        print(res[i], end=" ")

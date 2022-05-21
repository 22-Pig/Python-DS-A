class MyQueue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enQueue(self, item):
        self.items.insert(0, item)

    def deQueue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def ring(a, b):
    q = MyQueue()
    for i in range(1, a + 1):
        q.enQueue(i)

    while q.size() > 1:
        for i in range(b):
            if i == b - 1:
                print(q.deQueue(), end=" ")
            else:
                q.enQueue(q.deQueue())
        b += 1

    return q.deQueue()


x, y = map(int, input().split())
print(ring(x, y), end=" ")

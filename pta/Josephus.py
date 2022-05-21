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


while True:
    try:
        a = int(input())
        q = MyQueue()
        for i in range(1, a + 1):
            q.enQueue(i)

        while q.size() > 1:
            for i in range(2):
                q.enQueue(q.deQueue())
            q.deQueue()

        print(q.deQueue())
    except:
        break
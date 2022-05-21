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


a = int(input())
q = MyQueue()

ls = []
for i in range(a):
    ls.append(input())

for i in ls:
    # 操作1，将要添加的元素添加到队列的尾部
    if i[0] == "1":
        q.enQueue(int(i[2:]))
    # 操作2，若队列为空，则输出 “Invalid”,否则请输出队首元素，并将这个元素从队列中删除。
    elif i == "2":
        if q.isEmpty():
            print("Invalid")
        else:
            print(q.deQueue())
    # 操作3，输出队列长度。 每个输出项最后换行。
    elif i == "3":
        print(q.size())
    # 操作4，输出队列中每个元素，元素之间用空格分隔，最后一个元素后面没有空格
    elif i == "4":
        for i in range(q.size() - 1):
            elem = q.deQueue()
            print(elem, end=" ")
            q.enQueue(elem)
        elem = q.deQueue()
        print(elem)
        q.enQueue(elem)

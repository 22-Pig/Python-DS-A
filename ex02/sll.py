# 单链表的操作
# 结点初始化函数
class LNode(object):
    # 初始设置下一节点为空
    def __init__(self, data, p=None):
        self.data = data
        self.next = p


# 创建单链表类
class LinkList(object):

    def __init__(self):
        # 先初始化一个头节点，为None
        self.head = None
        self.length = 0

    # 链表初始化函数, 方法类似于尾插
    def initList(self, data):
        # 创建头结点
        # 这个节点创建完，包含两部分：是个既包含节点值，也包含节点所链接的下一个节点
        self.head = LNode(data[0])
        # 初始化p指向头节点
        p = self.head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = LNode(i)
            p.next = node
            # 构建完一个节点，移动到构建完的节点上，继续向后构建节点
            p = p.next

    # 判断链表是否为空
    def isEmpty(self):
        if self.head.next == 0:
            print("Empty List!")
            return True
        else:
            return False

    # 取链表长度
    def getLength(self):
        if self.isEmpty():
            exit(0)

        p = self.head
        len = 0
        while p:
            len += 1
            p = p.next
        return len

    # 遍历链表
    def traveList(self):
        if self.isEmpty():
            exit(0)
        # print("link list traveling result:")
        p = self.head
        while p:
            print(p.data, end=' ')
            p = p.next

    # 链表插入数据函数（首部）
    def addElem(self, key):
        # 遍历找到索引值为 index 的结点后, 在其后面插入结点
        node = LNode(key)
        # 新结点指针指向原头部结点
        node.next = self.head
        # 头部结点指针修改为新结点
        self.head = node

    # 链表插入数据函数（尾部）
    def appendElem(self, key):
        node = LNode(key)
        # 先判断是否为空链表
        if self.isEmpty():
            self.head = node
        else:
            # 不是空链表，则找到尾部，将尾部 next 结点指向新结点
            p = self.head
            while p.next is not None:
                p = p.next
            p.next = node

    # 链表插入数据函数（定位）
    def insertElem(self, key, index):
        if self.isEmpty():
            exit(0)
        if index < 0 or index > self.getLength() - 1:
            print("\rKey Error! Program Exit.")
            exit(0)

        p = self.head
        i = 0
        while i <= index:
            pre = p
            p = p.next
            i += 1

        # 遍历找到索引值为 index 的结点后, 在其后面插入结点
        node = LNode(key)
        pre.next = node
        node.next = p

    # 链表删除数据函数（首部）
    def pop(self):
        if self.head == None:
            return False
        else:
            # 保存首元素的地址
            n = self.head.data
            # 将首指针指向下一节点
            self.head = self.head.next
        # 返回被删除的元素
        return n

    # 链表删除数据函数（尾部）
    def poplast(self):
        # 空链表
        if self.head == None:
            return False
        # 若只有一个结点，则将首指针设为None
        elif self.head.next == None:
            e = self.head.data
            self.head.next = None
            return e
        # 若有两个及以上个结点，则遍历至倒数第二个结点
        else:
            p = self.head
            while p.next.next != None:
                p = p.next
            e = p.next.data
            p.next = None
            return e

    # 链表删除数据函数（定位）
    def deleteElem(self, index):
        if self.isEmpty():
            exit(0)
        if index < 0 or index > self.getLength() - 1:
            print("\rValue Error! Program Exit.")
            exit(0)

        i = 0
        p = self.head
        # 遍历找到索引值为 index 的结点
        while p.next:
            pre = p
            p = p.next
            i += 1
            if i == index:
                pre.next = p.next
                p = None
                return True

        # p的下一个结点为空说明到了最后一个结点, 删除之即可
        pre.next = None

    # 链表查找
    def findElem(self, key):
        if self.isEmpty():
            exit(0)
        ret = 0
        p = self.head
        while p != None:
            if p.data == key:
                return ret
            ret += 1
            p = p.next
        return False

    # 链表逆置
    def reverse(self):
        p = self.head

        self.head = self.head.next
        # 必须要将原先的首结点的next设为0，否则将在遍历时出现死循环
        p.next = None
        while self.head != None:
            q = p
            p = self.head
            self.head = self.head.next
            p.next = q
        self.head = p


def main():
    # 初始化链表与数据
    data = [1, 2, 3, 4, 5]
    l = LinkList()
    l.initList(data)
    print("\r初始化链表与数据")
    l.traveList()

    # 在首部插入值为0的结点
    print("\r在首部插入值为0的结点")
    l.addElem(0)
    l.traveList()

    # 在尾部插入值为99的结点
    print("\r在尾部插入值为99的结点")
    l.appendElem(99)
    l.traveList()

    # 插入结点到索引为2之后, 值为33
    print("\r插入结点到索引为2之后, 值为33")
    l.insertElem(33, 2)
    l.traveList()

    # 删除首部结点
    print("\r删除首部结点")
    l.pop()
    l.traveList()
    # print("\r" + str(l.pop()))

    # 删除尾部结点
    print("\r删除尾部结点")
    l.poplast()
    l.traveList()

    # 删除索引值为2的结点
    print("\r删除索引值为2的结点")
    l.deleteElem(2)
    l.traveList()

    # 查找元素值为2的结点的位置
    print("\r查找元素值为2的结点的位置")
    print(l.findElem(2))

    # 链表逆置
    print("\r链表逆置")
    l.reverse()
    l.traveList()


if __name__ == '__main__':
    main()

# 栈的链式存储
class StackNode:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkStack(object):

    def __init__(self):
        self.top = StackNode()
        self.length = 0

    # 获取长度
    def getLengthStack(self):
        return self.length

    # 判断链栈是否为空
    def isEmptyStack(self):
        if self.top == None:
            iTop = True
        else:
            iTop = False
        return iTop

    # 入栈
    def pushStack(self, data):
        tStackNode = StackNode(data)
        if self.isEmptyStack():
            self.top = tStackNode
        else:
            tStackNode.next = self.top
            self.top = tStackNode
        self.length += 1
        print("当前入栈的元素为：", data)

    # 出栈
    def popStack(self):
        if self.isEmptyStack():
            raise IndexError('stack is null')
        else:
            self.length -= 1
            data = self.top.data
            self.top = self.top.next
            return data

    # 获取栈顶元素
    def getTopStack(self):
        if self.isEmptyStack():
            print("栈为空")
        else:
            return self.top.data

    # 创建一个链栈
    def createStackByInput(self):
        data = input("请输入元素(\"-1\"表示结束)：")
        while data != "-1":
            self.pushStack(data)
            data = input("请输入元素(\"-1\"表示结束)：")
        print("输入结束")

    def findStack(self):
        element = input("请输入要寻找的元素：")
        i = 0
        tStackNode = self.top
        result = self.popStack()
        while tStackNode.next != None and element != result:
            tStackNode = tStackNode.next
            result = self.popStack()
            i += 1
        if element == result:
            print("已找到，距栈顶", i, "个位置")
        else:
            print("链栈中无此元素")

    # 遍历链栈
    def traveStack(self):
        ret = []
        if self.isEmptyStack():
            exit(0)
        tStackNode = self.top
        while tStackNode.data:
            ret.append(tStackNode.data)
            tStackNode = tStackNode.next
        ret.reverse()
        print("当前栈表:", ret)


def main():
    Ls = LinkStack()
    Ls.createStackByInput()
    Ls.traveStack()
    Ls.findStack()


if __name__ == '__main__':
    main()
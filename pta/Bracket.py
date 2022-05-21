class Stack:

    def __init__(self):
        self.items = []

    #判断栈是否为空
    def isEmpty(self):
        return self.items == []

    #入栈
    def push(self, item):
        self.items.append(item)

    #出栈
    def pop(self):
        return self.items.pop()

    #取栈顶元素
    def peek(self):
        return self.items[len(self.items) - 1]

    #取栈的大小
    def size(self):
        return len(self.items)


s = Stack()
word = input()
f = True
for c in word:
    if c == "(" or c == "[" or c == "{":  #如果匹配左括号，则入栈
        s.push(c)
    elif c == ")":  #如果匹配右括号，则出栈
        if s.isEmpty():
            f = False
            break
        if s.peek() == "(":
            s.pop()
        else:
            f = False
            break
    elif c == "]":
        if s.isEmpty():
            f = False
            break
        if s.peek() == "[":
            s.pop()
        else:
            f = False
            break
    elif c == "}":
        if s.isEmpty():
            f = False
            break
        if s.peek() == "{":
            s.pop()
        else:
            f = False
            break

if not s.isEmpty():
    f = False

print("yes" if f else "no")
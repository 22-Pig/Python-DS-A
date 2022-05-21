import queue


class TreeNode(object):
    # 结点初始设置
    def __init__(self, data, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


class BiTree:
    # 初始化根
    def __init__(self, root=None):
        self.root = root

    def create(self):
        data = input("Enter a value:")
        if data == '#':
            return None
        tNode = TreeNode(data)
        if self.root == None:
            self.root = tNode
        tNode.lchild = self.create()
        tNode.rchild = self.create()
        return tNode

    def isEmpty(self):
        if self.root is None:
            return True
        else:
            return False

# 先序遍历

    def PreOrder(self, node):
        if node == None:
            return
        print(node.data, end=" ")
        self.PreOrder(node.lchild)
        self.PreOrder(node.rchild)

# 中序遍历

    def InOrder(self, node):
        if node == None:
            return
        self.InOrder(node.lchild)
        print(node.data, end=" ")
        self.InOrder(node.rchild)
# 后序遍历

    def PostOrder(self, node):
        if node == None:
            return
        self.PostOrder(node.lchild)
        self.PostOrder(node.rchild)
        print(node.data, end=" ")


# 层次遍历

    def LevelOrder(self, node):
        qu = queue.Queue()
        qu.put(node)
        while not qu.empty():
            node = qu.get()
            print(node.data, end=" ")
            if node.lchild:
                qu.put(node.lchild)
            if node.rchild:
                qu.put(node.rchild)

    def countBiTNode(self, node):
        #当二叉树为空时直接返回0
        if node is None:
            return 0
        #当二叉树只有根，无左右孩子时，根节点就是一个叶子节点
        elif node.lchild == None and node.rchild == None:
            return 1
        #当二叉树只有单个左或者右孩子时，进行递归查找
        elif (node.lchild == None and node.rchild != None
              or node.rchild == None and node.lchild != None):
            return 1 + self.countBiTNode(node.lchild) + self.countBiTNode(
                node.rchild)
        #其他情况
        else:
            M = self.countBiTNode(node.lchild)
            N = self.countBiTNode(node.rchild)
            return M + N


def main():
    b = BiTree()
    b.create()
    b.PreOrder(b.root)
    print("先序遍历")
    b.InOrder(b.root)
    print("中序遍历")
    b.PostOrder(b.root)
    print("后序遍历")
    b.LevelOrder(b.root)
    print("层序遍历")

    print("二叉树中的叶子个数和度为1的结点数:")
    ret = b.countBiTNode(b.root)
    print(ret)


if __name__ == '__main__':
    main()
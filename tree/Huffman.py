class HuffmanTreeNode(object):

    def __init__(self,
                 data='#',
                 weight=-1,
                 parent=None,
                 lchild=None,
                 rchild=None):
        self.data = data
        self.weight = weight
        self.parent = parent
        self.lchild = lchild
        self.rchild = rchild


class HuffmanTree:

    def __init__(self, dataList):
        self.nodes = []
        # 按权重从大到小进行排列
        for val in dataList:
            newNode = HuffmanTreeNode()
            newNode.data = val[0]
            newNode.weight = val[1]
            self.nodes.append(newNode)
        self.nodes = sorted(self.nodes,
                            key=lambda node: node.weight,
                            reverse=True)

    def CreateHuffmanTree(self):
        # TreeNode = self.nodes[:]  变量TreeNode, 这个相当于深拷贝, TreeNode变化不影响nodes
        # TreeNode = self.nodes     指针TreeNode与nodes共享一个地址, 相当于浅拷贝, TreeNode变化会影响nodes
        TreeNode = self.nodes[:]
        if len(TreeNode) > 0:
            while len(TreeNode) > 1:
                # 取列表尾端即权重最小的结点
                letfNode = TreeNode.pop()
                rightNode = TreeNode.pop()
                # 建立新结点
                newNode = HuffmanTreeNode()
                newNode.lchild = letfNode
                newNode.rchild = rightNode
                newNode.weight = letfNode.weight + rightNode.weight

                letfNode.parent = newNode
                rightNode.parent = newNode

                # 将生成的新结点按照权重插入列表
                self.InsertTreeNode(TreeNode, newNode)
            return TreeNode[0]

    def InsertTreeNode(self, TreeNode, newNode):
        length = len(TreeNode)
        if length > 0:
            temp = length - 1
            while temp >= 0:
                if TreeNode[temp].weight > newNode.weight:
                    TreeNode.insert(temp + 1, newNode)
                    return True
                temp -= 1
        TreeNode.insert(0, newNode)

# 先序遍历

    def PreOrder(self, hufTree):
        if hufTree == None:
            return
        print(hufTree.weight, end=" ")
        self.PreOrder(hufTree.lchild)
        self.PreOrder(hufTree.rchild)

# 哈夫曼编码

    def HuffmanEncode(self, Root):
        TreeNode = self.nodes[:]
        codeResult = []
        for i in range(len(TreeNode)):
            temp = TreeNode[i]
            codeLeaf = [temp.data]
            code = ''
            while temp is not Root:
                if temp.parent.lchild is temp:
                    # 左分支
                    code = '0' + code
                else:
                    # 右分支
                    code = '1' + code
                temp = temp.parent
            codeLeaf.append(code)
            codeResult.append(codeLeaf)
        return codeResult


# 哈夫曼解码

    def HuffmanDecode(self, hufCode, cipherText):
        temp = ''
        decodeResult = []
        for i in cipherText:
            temp += i
            for j in range(len(hufCode)):
                if (temp == hufCode[j][1]):
                    code = [temp]
                    code.append(hufCode[j][0])
                    decodeResult.append(code)
                    temp = ""
                    break
        return decodeResult

if __name__ == '__main__':
    treeObj = HuffmanTree([('A', 154), ('B', 33), ('C', 22), ('D', 2),
                           ('E', 51), ('F', 17), ('G', 7), ('H', 10)])
    hufTree = treeObj.CreateHuffmanTree()

    print("哈夫曼树先序遍历:")
    treeObj.PreOrder(hufTree)

    print("\n哈夫曼编码:")
    hufCode = treeObj.HuffmanEncode(hufTree)
    for i in range(len(hufCode)):
        print('{0}: {1}'.format(hufCode[i][0], hufCode[i][1]))

    cipherText = input('请输入一串由0和1构成的字符串\n')
    decodeTable = treeObj.HuffmanDecode(hufCode, cipherText)
    for i in range(len(decodeTable)):
        print('{0}: {1}'.format(decodeTable[i][0], decodeTable[i][1]))

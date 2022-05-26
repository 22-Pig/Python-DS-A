# 定义图中顶点
class GraphVertex():
    # 初始化
    def __init__(self, data=None):
        self.data = data
        self.next = None


# 定义图结构
class Graph():
    # 初始化
    def __init__(self):
        self.graph = []

    # 向图中插入顶点
    def InsertVertex(self, newVertex):
        self.graph.append(newVertex)
        return self.graph

    # 创建图的邻接链表
    def CreateGraphAdjacencyList(self):
        SerachVertexList = []
        for vertex in self.graph:
            SerachVertexList.append(vertex.data)

        # 防止比较图中顶点时与if判断发生冲突
        SerachVertexList.append("#")

        # 找到图中的每一个顶点
        for vertex in self.graph:
            CurrentVertex = vertex
            print("请输入%s的邻接顶点(以'#'结束)" % CurrentVertex.data)
            while True:
                # 初始化每个顶点的邻接顶点
                ArcNode = GraphVertex()
                end = input(">>>")
                if CurrentVertex.data == end:
                    print("%s的邻接顶点不包括其自身,请重新输入..." % CurrentVertex.data)
                    continue
                if end not in SerachVertexList:
                    print("输入有误,%s不是该图中的顶点" % end)
                    continue
                if end == "#":
                    break
                else:
                    # 新建邻接顶点
                    ArcNode.data = end
                    # 尾插法插入当前顶点
                    ArcNode.next = CurrentVertex.next
                    CurrentVertex.next = ArcNode
                    # 指向当前顶点的邻接顶点
                    CurrentVertex = CurrentVertex.next

    # 打印邻接链表
    def PrintGraphAdjacencyList(self):
        for vertex in self.graph:
            print("顶点%s的邻接链表：" % vertex.data, vertex.data, end=" ")
            while vertex.next != None:
                print("--->", vertex.next.data, end="")
                vertex = vertex.next
            print("")


if __name__ == '__main__':
    n = int(input("请输入图中顶点的个数："))
    #实例化图
    MGraph = Graph()
    #创建顶点
    for i in range(0, n):
        vertex = input("请输入顶点：")
        #实例化图顶点
        VertexNode = GraphVertex(vertex)
        #将顶点添加至图中
        MGraph.InsertVertex(VertexNode)

    print("图中所有顶点：")
    for VertexNode in MGraph.graph:
        print(VertexNode.data, end='\t')
    print("")
    #创建图的邻接链表
    MGraph.CreateGraphAdjacencyList()
    #打印图的邻接链表
    MGraph.PrintGraphAdjacencyList()

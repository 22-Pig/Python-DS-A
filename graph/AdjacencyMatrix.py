# 定义图结构，初始化n * n的二维数组（n为图的顶点个数）
class Graph():
    # 初始化
    def __init__(self, n):
        self.vertex = []
        self.graph = [[0] * n for j in range(0, n)]

    # 向图中插入顶点
    def InsertVertex(self, n):
        vertexList = self.vertex
        for i in range(0, n):
            newVertex = input("请输入顶点的值：")
            if newVertex != None and newVertex != "#":
                vertexList.append(newVertex)

        return vertexList

    # 创建图的邻接矩阵
    def CreateGraphMatrix(self, vertexList):
        while True:
            start = input("请输入边的起始顶点(以'#'结束)：")
            end = input("请输入边的终止顶点(以'#'结束)：")
            weight = input("请输入边对应的权值：")
            if start == "#" and end == "#":
                break
            if start == end and (start != "#" and end != "#"):
                print("图的邻接矩阵不存在顶点到自身的边")
                continue
            if (start not in vertexList) or (end not in vertexList):
                print("输入有误,输入顶点不在图中,请重新输入...")
                continue

            else:
                i = vertexList.index(start)
                j = vertexList.index(end)
                if self.graph[i][j] == 0:
                    self.graph[i][j] = int(weight)
                    self.graph[j][i] = self.graph[i][j]

        return self.graph

    # 打印图的邻接矩阵
    def PrintGraphMatrix(self, n):
        GraphMatrix = self.graph
        # for i in range(0, n):
        #     print(GraphMatrix[i], end='\n')
        for row in GraphMatrix:
            print("".join(["{:^{len}}".format(elem, len=5) for elem in row]))


if __name__ == '__main__':

    n = int(input("请输入顶点的个数："))
    # 实例化图
    MGraph = Graph(n)
    # 向图中插入顶点
    vertexes = MGraph.InsertVertex(n)
    print("图中所有顶点：", vertexes)
    #构造图的邻接矩阵
    MGraph.CreateGraphMatrix(vertexes)
    #打印邻接矩阵
    MGraph.PrintGraphMatrix(n)

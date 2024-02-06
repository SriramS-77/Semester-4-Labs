class Graph:
    def __init__(self):
        self.matrix = []
        self.list = {}
        self.v = 0
    def addVertex(self):
        self.v += 1
        self.list[self.v] = []
        self.matrix.append([0 for i in range(self.v)])
        for i in range(self.v - 1):
            self.matrix[i].append(0)
    def addEdge(self, v1, v2, w):
        self.matrix[v1-1][v2-1] = w
        self.list[v1].append([v2, w])
    def displayMatrix(self):
        for i in range(len(self.matrix)):
            print(self.matrix[i])
    def displayList(self):
#        for i in self.list.keys():
#            print(self.list[i])
        print(self.list)

def main():
    g = Graph()
    g.addVertex()
    g.addVertex()
    g.addVertex()
    g.addVertex()
    g.addEdge(1, 2, 1)
    g.addEdge(1, 3, 1)
    g.addEdge(2, 3, 3)
    g.addEdge(3, 4, 4)
    g.addEdge(4, 1, 5)
    print("Adjacency List:")
    g.displayList()
    print("Adjacency Matrix:")
    g.displayMatrix()

if __name__ == "__main__":
    main()
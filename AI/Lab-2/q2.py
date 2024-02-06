class Graph:
    def __init__(self):
        self.list = dict()
        self.v = 0
    def addVertex(self):
        self.v += 1
        self.list[self.v] = []
    def addEdge(self, v1, v2, w):
        self.list[v1].append((v2,w))
    def displayGraph(self):
        for i in self.list:
            l = self.list[i]
            if len(l)==0:
                print(f'{i}--->None', end=" ")
            for j in l:
                print(f"({i}--->{j[0]}, {j[1]})", end=" ")
            print()

def main():
    g = Graph()
    g.addVertex()
    g.addVertex()
    g.addVertex()
    g.addVertex()
    g.addVertex()
    g.addVertex()
    g.addEdge(1,2,6)
    g.addEdge(2,3,7)
    g.addEdge(3,1,5)
    g.addEdge(3,2,4)
    g.addEdge(4,3,10)
    g.addEdge(5,6,1)
    g.addEdge(6,5,3)
    g.displayGraph()

if __name__ == "__main__":
    main()
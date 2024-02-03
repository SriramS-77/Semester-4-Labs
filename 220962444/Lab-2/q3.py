alpha = ['A', 'B', 'C', 'D', 'E', 'F']

class Graph:
    def __init__(self):
        self.matrix = list()
        self.list = dict()
        self.v = 0
    def addVertex(self):
        self.v += 1
        self.list[self.v] = []
        self.matrix.append([0 for i in range(self.v)])
        for i in range(self.v-1):
            self.matrix[i].append(0)
    def addEdge(self, v1, v2):
        self.list[v1].append(v2)
        self.list[v2].append(v1)
        self.matrix[v1-1][v2-1] = self.matrix[v2-1][v1-1] = 1
    def displayGraph(self):
        print("\nAdjacency List:\n")
        for i in self.list:
            l = self.list[i]
            if len(l)==0:
                print(f'{alpha[i-1]} :  None')
            else:
                print(f'{alpha[i-1]} : ', [alpha[i-1] for i in sorted(l)])
        print("\nAdjacency Matrix:\n")
        for i in self.matrix:
            print(*i)

def main():
    g = Graph()
    g.addVertex()
    g.addVertex()
    g.addVertex()
    g.addVertex()
    g.addVertex()

    g.addEdge(1,2)
    g.addEdge(1,3)
    g.addEdge(1,5)
    g.addEdge(3,2)
    g.addEdge(5,3)
    g.addEdge(3,4)
 #   g.addEdge(4,5)
    g.addEdge(4,2)
 
    g.displayGraph()

if __name__ == "__main__":
    main()
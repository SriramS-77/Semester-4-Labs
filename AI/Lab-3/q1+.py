class Graph:
    def __init__(self):
        self.matrix = list()
        self.list = dict()
        self.v = 0
    def addVertex(self):
        self.v += 1
        self.list[self.v-1] = []
        self.matrix.append([0 for i in range(self.v)])
        for i in range(self.v-1):
            self.matrix[i].append(0)
    def addEdge(self, v1, v2):
        self.list[v1].append(v2)
        self.matrix[v1][v2] = 1

    def displayGraph(self):
        print("\nAdjacency List:\n")
        for i in self.list:
            l = self.list[i]
            if len(l)==0:
                print(f'{i} :  None')
            else:
                print(f'{i} : ', [i for i in sorted(l)])
        print("\nAdjacency Matrix:\n")
        for i in self.matrix:
            print(*i)

    def sort(self):
        lv = list(range(self.v))
        self.sortedVertices = []
        while len(lv)!=0:
            for i in range(self.v):
                if i in self.sortedVertices:
                    continue
                all = 0
                for j in range(self.v):
                    if j in self.sortedVertices:
                        continue
                    if self.matrix[j][i]==1:
                        all=1
                if all==0:
                    start = i
                    break
            
            self.sortedVertices.append(start)
            lv.remove(start)


def main():
    g = Graph()
    g.addVertex()
    g.addVertex()
    g.addVertex()
    g.addVertex()
    g.addVertex()
    g.addVertex()

    g.addEdge(2,3)
    g.addEdge(3,1)
    g.addEdge(4,0)
    g.addEdge(4,1)
    g.addEdge(5,0)
    g.addEdge(5,2)
 
    g.displayGraph()

    g.sort()

    print(f"\nSorted Vertices: {g.sortedVertices}")

if __name__ == "__main__":
    main()

'''   
    def detectCycle(self, start):
        stack=[]
        visited=[]
        stack.append(start)
        visited.append(start)
        while(len(stack)!=0):
            v = stack.pop()    
            for i in self.list[v]:
                if i not in visited:
                    stack.append(v)
                    stack.append(i)
                    visited.append(i)
                    break
        return visited
'''
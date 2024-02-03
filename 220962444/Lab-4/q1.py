class Graph:
    def __init__(self):
        self.matrix = list()
        self.list = dict()
        self.v = 0
        self.sortedVertices = []
        self.indegree = None
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

    def get_indegree(self):
        if self.indegree:
            return
        self.indegree = {}
        for i in range(self.v):
            self.indegree[i] = 0
            for j in range(self.v):
                if self.matrix[j][i] == 1:
                    self.indegree[i] += 1

    def sort(self, prev_visited=None):
        self.get_indegree()
        start = -1
        for i in range(self.v):
            if i not in self.sortedVertices and self.indegree[i] == 0:
                start = i
                break
        if start==-1:
            print("Topological sort not possible!!!")
            self.sortedVertices = None
            return None
        queue = [start]
        if prev_visited == None:
            visited=[start]
        else:
            visited = prev_visited

        while len(queue)!=0:
            v = queue.pop(0)
            self.sortedVertices.append(v) 
            for i in self.list[v]:
                self.indegree[i] -= 1
                if i not in self.sortedVertices and self.indegree[i] == 0:
                    queue.append(i)
                
        if len(self.sortedVertices) != self.v:
            self.sort(visited) 
        else:
            print("\n\nTopological sort: ", self.sortedVertices)
            return self.sortedVertices
                    

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
#    g.addEdge(1,5)
 
    g.displayGraph()

    g.sort()

#    print(f"\nSorted Vertices: {g.sortedVertices}")

if __name__ == "__main__":
    main()

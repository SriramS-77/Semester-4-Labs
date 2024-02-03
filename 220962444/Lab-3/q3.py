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
    def addVertices(self, n):
        for i in range(n):
            self.addVertex()

    def addEdge(self, v1, v2):
        self.list[v1].append(v2)
        self.list[v2].append(v1)
        self.matrix[v1-1][v2-1] = self.matrix[v2-1][v1-1] = 1
    def addEdges(self, edges):
        for edge in edges:
            self.addEdge(edge[0], edge[1])

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
        
    def getPath(self, start, goal):
        stack=[start]
        visited=[start]
        while(len(stack)!=0):
            v = stack.pop()    
            for i in self.list[v]:
                if i==goal:
                    print("Goal reached!!!")
                    stack += [v, goal]
                    print("Path: ", stack)
                    return stack
                
                if i not in visited:
                    stack.append(v)
                    stack.append(i)
                    visited.append(i)
                    break
        return None


def main():
    g = Graph()
    g.addVertices(20)
    g.addEdges([(1,2), (2,3), (3,8), (8,7), (1,6), (6,11), (11,12), (12,17), (17,16), (17,18), (18,19), (19,14), (13,14),
                (9,14), (9,10), (10,15), (15,20), (10,5), (5,4)])
 
#    g.displayGraph()
    g.getPath(2, 20)


if __name__ == "__main__":
    main()
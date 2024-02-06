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
        
    def detectCycle(self, start):
        stack=[]
        visited=[]
        stack.append(start)
        visited.append(start)
        while(len(stack)!=0):
            v = stack.pop()    
            for i in self.list[v]:
                if i in stack:
                    print("Cycle detected!!!")
                    return True
                if i not in visited:
                    stack.append(v)
                    stack.append(i)
                    visited.append(i)
                    break
        return False


def main():
    g = Graph()
    g.addVertex()
    g.addVertex()
    g.addVertex()
    g.addVertex()

    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(1,2)
    g.addEdge(2,0)
    g.addEdge(2,3)
    g.addEdge(3,3)
 
#    g.displayGraph()

    print(g.detectCycle(2))

if __name__ == "__main__":
    main()
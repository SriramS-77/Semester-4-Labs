lst = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}

class Node:
    def __init__(self, node, w=0, prev_node=None):
        if prev_node is None:
            self.cost = 0
            self.path = [node]
        else:
            self.cost = prev_node.cost + w
            self.path = prev_node.path + [node]

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
    def addEdge(self, v1, v2, w):
        self.list[v1].append((v2,w))
        self.matrix[v1][v2] = w

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

    def search(self):
        queue = list()
        for i in range(self.v):
            queue.append(Node(i))
        path = None

        while len(queue)!=0:
            v: Node = queue.pop(0)
            if len(v.path) == self.v:
                if path is None:
                    path = v
                elif v.cost < path.cost:
                    path = v
                    continue
            for i, w in self.list[v.path[-1]]:
                if i not in v.path:
                    queue.append(Node(i, w, v))
        print(f'\n\nOptimal path is ', [lst[i] for i in path.path])
        print(f'Cost of path is {path.cost}')
        return path
                    

def main():
    g = Graph()

    g.addVertex()
    g.addVertex()
    g.addVertex()
    g.addVertex()

    g.addEdge(0,1,2)
    g.addEdge(0,2,3)
    g.addEdge(0,3,1)
    g.addEdge(1,0,2)
    g.addEdge(1,2,4)
    g.addEdge(1,3,2)
    g.addEdge(2,0,3)
    g.addEdge(2,1,4)
    g.addEdge(2,3,3)
    g.addEdge(3,0,1)
    g.addEdge(3,1,2)
    g.addEdge(3,2,3)
 
    g.displayGraph()

    g.search()


if __name__ == "__main__":
    main() 

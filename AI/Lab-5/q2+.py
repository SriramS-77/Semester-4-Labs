class Node:
    def __init__(self, node, w = None, prev_node = None):      
        if prev_node is None:
            self.path = [node]
            self.cost = 0
        else:
            self.path = prev_node.path + [node]
            self.cost = prev_node.cost + w
            
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
    def addVerices(self, n):
        for i in range(n):
            self.addVertex()
    def addEdge(self, v1, v2, w):
        self.list[v1].append((v2, w))
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
    
    def path(self, start, goals):
        queue = [Node(start)]
        visited = []
        while(len(queue) != 0):
            if len(goals) == 0:
                print('\nAll the goal states reached!!!')
                return True
            small = 0
            for i in range(len(queue)):
                if queue[i].cost < queue[small].cost:
                    small = i
            top = queue.pop(small)
            visited.append(top.path[-1])
            if top.path[-1] in goals:
                print(f"\n\nGoal state {top.path[-1]} reached!!!")
                print(f"Cost = {top.cost}")
                print(f"Path = {top.path}")
                goals.remove(top.path[-1])
            for i in self.list[top.path[-1]]:
                node, w = i[0], i[1]
                if node not in visited:
                    queue.append(Node(node, w, top))
                else:
                    for j in queue:
                        if j.path[-1] == node and j.cost > top.cost + w:
                            index = queue.index(j)
                            queue[index] = Node(node, w, top)

                    

def main():
    g = Graph()

    g.addVerices(10)

    g.addEdge(0,1,5)
    g.addEdge(0,2,9)
    g.addEdge(0,4,6)
    g.addEdge(1,2,3)
    g.addEdge(1,7,9)
    g.addEdge(2,1,2)
    g.addEdge(2,3,1)
    g.addEdge(3,0,6)
    g.addEdge(3,8,5)
    g.addEdge(3,6,7)
    g.addEdge(4,3,2)
    g.addEdge(4,5,2)
    g.addEdge(5,9,7)
    g.addEdge(6,4,2)
    g.addEdge(6,9,8)
 
    g.displayGraph()

    g.path(0, [7,8,9])


if __name__ == "__main__":
    main()

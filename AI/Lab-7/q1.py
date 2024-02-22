lst = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J'}

class Node:
    def __init__(self, node, h, w = None, prev_node = None):
        self.node = node
        if prev_node is None:
            self.path = [node]
            self.cost = 0
        else:
            self.path = prev_node.path + [node]
            self.cost = prev_node.cost + w
        self.h_cost = self.cost + h

class Graph:
    def __init__(self):
        self.matrix = list()
        self.list = dict()
        self.heuristic = {}
        self.v = 0

    def get_h(self, node):
        return self.heuristic[node]

    def addVertex(self, h: int):
        self.v += 1
        self.heuristic[self.v - 1] = h
        self.list[self.v-1] = []
        self.matrix.append([0 for i in range(self.v)])
        for i in range(self.v-1):
            self.matrix[i].append(0)

    def addVertices(self, n):
        for i in n:
            self.addVertex(i)

    def addEdge(self, v1, v2, w):
        self.list[v1].append((v2, w))
        self.list[v2].append((v1, w))
        self.matrix[v1][v2] = self.matrix[v2][v1] = w

    def displayGraph(self):
        print("\nAdjacency List:\n")
        for i in self.list:
            l = self.list[i]
            if len(l)==0:
                print(f'{i} :  None')
            else:
                print(f'{i} : ', [(lst[i[0]], i[1]) for i in sorted(l)])
        print("\nAdjacency Matrix:\n")
        for i in self.matrix:
            print(*i)
    
    def path(self, start, goal):
        queue = [Node(start, self.heuristic[start])]
        visited = []
        while(len(queue) != 0):
            small = 0
            for i in range(len(queue)):
                if queue[i].h_cost < queue[small].h_cost:
                    small = i
            top: Node = queue.pop(small)
            visited.append(top.path[-1])
            if top.node == goal:
                print(f"\n\nGoal state {lst[goal]} reached from {lst[start]}!!!")
                print(f"Cost = {top.cost}")
                print(f"Path = ", [lst[i] for i in top.path])
                return True
            for i in self.list[top.node]:
                node, w = i[0], i[1]
                if node not in visited:
                    inserted = False
                    for j in queue:
                        if j.node == node and j.cost > top.cost + w:
                            inserted = True
                            index = queue.index(j)
                            queue[index] = Node(node, self.heuristic[node], w, top)
                            break
                    if not inserted:
                        queue.append(Node(node, self.heuristic[node], w, top))

                    
def main():
    g = Graph()

    g.addVertices([10, 8, 5, 7, 3, 6, 5, 3, 1, 0])

    g.addEdge(0,1,6)
    g.addEdge(1,2,3)
    g.addEdge(3,1,2)
    g.addEdge(3,2,1)
    g.addEdge(4,2,5)
    g.addEdge(3,4,8)
    g.addEdge(0,5,3)
    g.addEdge(5,6,1)
    g.addEdge(5,7,7)
    g.addEdge(6,8,3)
    g.addEdge(7,8,2)
    g.addEdge(4,8,5)
    g.addEdge(8,9,3)
    g.addEdge(4,9,5)
 
    g.displayGraph()

    g.path(0, 9)


if __name__ == "__main__":
    main()

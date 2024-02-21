lst = {0: 'S', 1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G1', 8: 'G2', 9: 'G3'}

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
        self.matrix[v1][v2] = w

    def displayGraph(self):
        print("\nAdjacency List:\n")
        for i in self.list:
            l = self.list[i]
            if len(l)==0:
                print(f'{lst[i]} :  None')
            else:
                print(f'{lst[i]} : ', [(lst[i[0]], i[1]) for i in sorted(l)])
        print("\nAdjacency Matrix:\n")
        for i in self.matrix:
            print(*i)
    
    def path(self, start, goals):
        queue = [Node(start, self.heuristic[start])]
        visited = []
        while(len(queue) != 0):
            small = 0
            for i in range(len(queue)):
                if queue[i].h_cost < queue[small].h_cost:
                    small = i
            top: Node = queue.pop(small)
            visited.append(top.path[-1])
            if top.node in goals:
                print(f"\n\nGoal state {lst[top.node]} reached from {lst[start]}!!!")
                print(f"Cost = {top.cost}")
                print(f"Path = ", [lst[i] for i in top.path])
                goals.remove(top.node)
                if len(goals) == 0:
                    print('\nAll the goal states have been reached!!!')
                    return True
            for i in self.list[top.node]:
                node, w = i[0], i[1]
                if node not in visited:
                    queue.append(Node(node, self.heuristic[node], w, top))
                else:
                    for j in queue:
                        if j.node == node and j.cost > top.cost + w:
                            index = queue.index(j)
                            queue[index] = Node(node, self.heuristic[node], w, top)

                    

def main():
    g = Graph()

    g.addVertices([5, 7, 3, 4, 6, 5, 6, 0, 0, 0])

    g.addEdge(0,1,5)
    g.addEdge(0,2,9)
    g.addEdge(1,2,3)
    g.addEdge(2,1,2)
    g.addEdge(2,3,1)
    g.addEdge(3,0,6)
    g.addEdge(3,6,7)    
    g.addEdge(0,4,6)
    g.addEdge(4,0,1)
    g.addEdge(4,3,2)
    g.addEdge(4,5,2)
    g.addEdge(6,4,2)
    g.addEdge(1,7,9)
    g.addEdge(3,8,5)
    g.addEdge(5,9,7)
    g.addEdge(6,9,8)

    g.displayGraph()

    g.path(0, [7, 8, 9])


if __name__ == "__main__":
    main()

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
        cost = -1
        queue = [(start, 0)]
        visited = []
        while(len(queue) != 0):
            if len(goals) == 0:
                print('\nAll the goal states reached!!!')
                return True
            small = 0
            for i in range(len(queue)):
                if queue[i][1] < queue[small][1]:
                    small = i
            top = queue.pop(small)
            visited.append(top[0])
            if top[0] in goals:
                print(f"\n\nGoal state {top[0]} reached!!!")
                print(f"Cost = {top[1]}")
                goals.remove(top[0])
            for i in self.list[top[0]]:
                node, w = i[0], i[1]
                if node not in visited:
                    queue.append((node, top[1]+w))
                else:
                    for j in queue:
                        if j[0] == node and j[1] > top[1] + w:
                            index = queue.index(j)
                            queue[index] = (node, top[1] + w)

                    

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

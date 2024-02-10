lst = ['Dunwich', 'Blaxhall', 'Harwich', 'Tiptree', 'Feering', 'Clacton', 'Maldon']

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

    def get_indegree(self):
        if self.indegree:
            return
        self.indegree = {}
        for i in range(self.v):
            self.indegree[i] = 0
            for j in range(self.v):
                if self.matrix[j][i] == 1:
                    self.indegree[i] += 1
    
    def path(self, start, goal):
        queue = [(start, 0)]
        visited = []
        while(len(queue) != 0):
            small = 0
            for i in range(len(queue)):
                if queue[i][1] < queue[small][1]:
                    small = i
            top = queue.pop(small)
            visited.append(top[0])
            if top[0] == goal:
                print(f"\n\nGoal state {lst[goal]} reached from {lst[start]}!!!")
                print(f"Cost = {top[1]}")
                return True
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

    g.addVerices(7)

    g.addEdge(0,1,17)
    g.addEdge(1,0,15)
    g.addEdge(2,0,53)
    g.addEdge(2,1,40)
    g.addEdge(2,3,31)
    g.addEdge(3,4,3)
    g.addEdge(3,5,29)
    g.addEdge(4,1,46)
    g.addEdge(4,6,11)
    g.addEdge(5,6,40)
    g.addEdge(5,2,17)
    g.addEdge(6,3,8)
 
    g.displayGraph()

    g.path(6, 0)


if __name__ == "__main__":
    main()

import random
import copy

goal = [[1,2,3],[8,0,4],[7,6,5]]
# goal = [[1,2,3], [4,5,6], [7,8,0]]

class Node:
    def __init__(self, node, w = None, prev_node = None):
        self.node = node
        if prev_node is None:
            self.path = [node]
            self.cost = 0
        else:
            self.path = prev_node.path + [node]
            self.cost = prev_node.cost + w
        self.h = get_heuristic(node)
        self.h_cost = self.cost + self.h
    
    def disp(self):
        print(f'Node -> h = {self.h}, h-cost -> {self.h_cost}')
        for i in self.node:
            print(i)

def get_heuristic(node):
    h = 0
    for i in range(len(node)):
        for j in range(len(node[0])):
            if node[i][j] != goal[i][j]:
                h += 1
    return h

def get_new_nodes(node):
    l = len(node)
    for i_ in range(len(node)):
        for j_ in range(len(node[0])):
            if node[i_][j_] == 0:
                i, j = i_, j_
    lst = list()
    if i - 1 >= 0:
        arr = copy.deepcopy(node)
        arr[i-1][j], arr[i][j] = arr[i][j], arr[i-1][j]
        lst.append(arr)
    if i + 1 < l:
        arr = copy.deepcopy(node)
        arr[i+1][j], arr[i][j] = arr[i][j], arr[i+1][j]
        lst.append(arr)
    if j - 1 >= 0:
        arr = copy.deepcopy(node)
        arr[i][j-1], arr[i][j] = arr[i][j], arr[i][j-1]
        lst.append(arr)
    if j + 1 < l:
        arr = copy.deepcopy(node)
        arr[i][j+1], arr[i][j] = arr[i][j], arr[i][j+1]
        lst.append(arr)
    return lst
    
def path(start):
    c = 0
    queue = [Node(start)]
    visited = []
    while(len(queue) != 0):
        small = 0
        for i in range(len(queue)):
            if queue[i].h < queue[small].h:
                small = i
        top: Node = queue.pop(small)
        print('Popped:')
        top.disp()
        visited.append(top.node)
        if top.h == 0:
            print(f"\n\nGoal state {top.node} reached from {start}!!!")
            print(f"Cost = {top.cost}")
            print(f"Path = ", [i for i in top.path])
            print(f'Iteration: {c}')
            break
        
        for i in get_new_nodes(top.node):
            if i not in visited:
                print('Inserting in queue:')
                queue.append(Node(i, 1, top))
                queue[-1].disp()
        print('Loop ended -> length of queue = ', len(queue), '*'*30)
        c += 1
        if c==1000:
            queue.clear()
            path(random_initialiaze())
            

def random_initialiaze():
    initial = list(range(9))
    random.shuffle(initial)
    arr = list()
    arr.append(initial[:3])
    arr.append(initial[3:6])
    arr.append(initial[6:9])
    return arr


def main():
    arr = random_initialiaze()

    #arr = [[1,2,3], [0,4,6], [7,5,8]]

    print('Initial puzzle:', arr)
    path(arr)
    
if __name__ == "__main__":
    main()

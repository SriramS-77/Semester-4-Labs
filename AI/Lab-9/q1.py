class Node:
    def __init__(self, node, w = None, prev_node = None):
        self.node = node
        if prev_node is None:
            self.path = [node]
            self.cost = 0
        else:
            self.path = prev_node.path + [node]
            self.cost = prev_node.cost + w
            
def min(a, b):
    return (a if a < b else b)

def generate_states(n: Node, max):
    states = []
    node = n.node
    if node[0] != 0:
        states.append((0, node[1]))
    if node[1] != 0:
        states.append((node[0], 0))
    if node[0] != max[0]:
        states.append((max[0], node[1]))
    if node[1] != max[1]:
        states.append((node[0], max[1]))
    if node[0] != 0 and node[1] != max[1]:
        shift = min(max[1] - node[1], node[0])
        states.append((node[0] - shift, node[1] + shift))
    if node[1] != 0 and node[0] != max[0]:
        shift = min(max[0] - node[0], node[1])
        states.append((node[0] + shift, node[1] - shift))
    print(states)
    return states


def path(start: tuple, max: tuple, goal: int):
    queue = [Node(start)]
    visited = []
    while(len(queue) != 0):
        top: Node = queue.pop(0)
        visited.append(top.node)
        for i in top.node:
            if i == goal:
                print(f"\n\nGoal state ({goal}, X) reached from {list(start)}!!!")
                print(f"Cost = {top.cost}")
                print(f"Path = ", [list(i) for i in top.path])
                return True
        for node in generate_states(top, max):
            if node not in visited:
                queue.append(Node(node, 1, top))
    print('Goal state not possible!!!')
    return False
                
def paths(start: tuple, max: tuple, goal: int):
    queue = [Node(start)]
    visited = []
    while(len(queue) != 0):
        top: Node = queue.pop(0)
        print('Top: ', top.node)
        visited.append(top.node)
        if top.node[0] == goal and top.node[1] == 0:
            print(f"\n\nGoal state ({goal}, X) reached from {list(start)}!!!")
            print(f"Cost = {top.cost}")
            print(f"Path = ", [list(i) for i in top.path])
            return True
        for node in generate_states(top, max):
            if node not in visited:
                queue.append(Node(node, 1, top))
    print('Goal state not possible!!!')
    return False
               
def main():
    paths((0, 0), (7, 3), 8)
    
if __name__ == "__main__":
    main()
class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    def enqueue(self, a):
        self.s1.append(a)
    def dequeue(self):
        if len(self.s2) == 0:
            self.s2 += reversed(self.s1)
            self.s1.clear()
        return self.s2.pop()
    def display(self):
        for i in reversed(self.s2):
            print(i, end=" ")
        for i in self.s1:
            print(i, end=" ")
        print()

def main():
    q = Queue()
    while(True):
        x = int(input("Enter choice: (1: Enqueue   2: Dequeue   3: Display   4: Exit) --- "))
        if x == 1:
            val = int(input("Enter value: "))
            q.enqueue(val)
        elif x == 2:
            val = q.dequeue()
            print(val, "was dequeued")
        elif x == 3:
            q.display()
        else:
            break

if __name__ == "__main__":
    main()
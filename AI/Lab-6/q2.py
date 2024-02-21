import random

def intersect(a, b):
    return (a[0] == b[0] or a[1] == b[1] or abs(a[0] - b[0]) == abs(a[1] - b[1]))

def get_max(lst):
    max = 0
    for i in range(len(lst)):
        if lst[i] > lst[max]:
            max = i
    return max

def initialize():
    arr = list()
    for i in range(8):
        while True:
            x, y = random.randint(0, 7), random.randint(0, 7)
            if (x, y) in arr:
                continue
            else:
                arr.append((x, y))
                break
    return arr

def disp(arr):
    for i in range(8):
        for j in range(8):
            if (i, j) in arr:
                print('1 ', end='')
            else:
                print('0 ', end='')
        print()

def intersection(arr):
    cost = 0
    cost_arr = [0 for i in range(len(arr))]
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if intersect(arr[i], arr[j]):
                cost_arr[i] += 1
                cost += 1
    return cost_arr, cost

iterations = 0

def hill_climb():
    global iterations
    arr = initialize()
    disp(arr)
    new_ele = None
    for i in range(10):
        iterations += 1
        cost_arr, cost = intersection(arr)
        print(f'Epoch {i} : Cost = {cost}\n')
        if cost == 0:
            print('Success!!!')
            print(f'\nRequired Iterations = {iterations}\n')
            return arr
        index = get_max(cost_arr)
        new_ele = arr[index]
        for i in range(len(arr)):
            for j in range(len(arr)):
                if (i, j) not in arr:
                    arr[index] = (i, j)
                    _, new_cost = intersection(arr)
                    if new_cost < cost:
                        cost = new_cost
                        new_ele = (i, j)
        arr[index] = new_ele
        disp(arr)
    print(f'Epoch {10} : Cost = {cost}\n')
    if cost != 0:
        print('\n\n\nNew Cycle!!!\n\n\n')
        hill_climb()

def main():
    hill_climb()

if __name__ == "__main__":
    main()
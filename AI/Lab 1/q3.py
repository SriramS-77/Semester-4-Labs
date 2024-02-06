def main():
    n = int(input("Enter number of elements: "))
    x = list(map(int, input("Enter list 1: ").split()))
    y = list(map(int, input("Enter list 2: ").split()))
    d = []
    for i in range(n):
        d.append(abs(x[i] - y[i]))
    print("Before bubble sort:\n", d)

    for i in range(n-1):
        for j in range(i+1, n):
            if d[i] > d[j]:
                d[i], d[j] = d[j], d[i]
    print("After bubble sort:\n", d)

if __name__ == "__main__":
    main()
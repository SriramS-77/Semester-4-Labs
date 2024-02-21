def f(x: int):
    return 2 * x ** 3 + 3 * x ** 2 - 100

def main():
    x = int(input("Enter starting value: "))
    print(f'Starting value for x = {x}')
    while True:
        prev = x
        if f(prev - 1) > f(x):
            x = prev - 1
        if f(prev + 1) > f(x):
            x = prev + 1
        if x == prev or x > 10 or x < -10:
            print(f'Solution is x = {prev} and f(x) = {f(prev)}')
            break

if __name__ == "__main__":
    main()
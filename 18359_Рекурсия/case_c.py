
def fib(n):
    if n < 2:
        return 1
    else:
        a, b = 1, 1
        for i in range(1, n):
            a, b = b, a + b
        return b


def main():
    n = int(input())

    last = fib(n)
    print(last)


def main_input():
    with open('input.txt', 'r') as f:
        n = int(f.read())

        last = fib(n)
        print(last)


if __name__ == "__main__":
    main()

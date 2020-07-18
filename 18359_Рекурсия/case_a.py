def fib(n):
    if n < 2:
        return 1

    return fib(n-1) + fib(n-2)


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

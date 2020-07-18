period_fib = [0, 1, 1, 2, 3, 5, 8, 3, 1, 4,
              5, 9, 4, 3, 7, 0, 7, 7, 4, 1,
              5, 6, 1, 7, 8, 5, 3, 8, 1, 9,
              0, 9, 9, 8, 7, 5, 2, 7, 9, 6,
              5, 1, 6, 7, 3, 0, 3, 3, 6, 9,
              5, 4, 9, 3, 2, 5, 7, 2, 9, 1]


def fib(n):
    if n == 1 or n == 2:
        return 1

    return fib(n-1) % 10 + fib(n-2) % 10


# def main1():
#     n = int(input())

#     last = fib(n)
#     print(last % 10)


def main():
    with open('input.txt', 'r') as f:
        n = int(f.read())

        last = fib(n+1)
        print(last)


if __name__ == "__main__":
    main()


def fact(n):
    res = 1
    while n > 1:
        res *= n
        n -= 1

    return res


def main():
    n = int(input())

    last = fact(n)
    print(last)


def main_input():
    with open('input.txt', 'r') as f:
        n = int(f.read())

        last = fact(n)
        print(last)


if __name__ == "__main__":
    main()

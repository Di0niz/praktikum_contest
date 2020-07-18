
def fact(n):
    if n > 1:
        return n * fact(n - 1)
    return 1


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

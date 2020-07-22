
def grammar(n, k):
    if n == 0:
        return '0'

    nxt = []
    kondr = grammar(n - 1, k)
    print(len(kondr), hex(int(kondr, 2)))
    for ch in kondr:
        if ch == '0':
            nxt.append('01')
        elif ch == '1':
            nxt.append('10')
    return ''.join(nxt)


def main():
    n = int(input())
    k = int(input())

    kondr = grammar(n, k)
    print(len(kondr), hex(int(kondr, 2)))


def main_input():
    with open(r'input.txt', 'r') as f:
        n = int(f.readline())
        k = int(f.readline())

        print(grammar(n, k)[k-1])


if __name__ == "__main__":
    main()

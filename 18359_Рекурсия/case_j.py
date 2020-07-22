
def grammar(n, k):
    if n == 0:
        return 0

    val = grammar(n - 1, k//2)

    return val if k % 2 == 0 else ~val & 1

    # nxt = []
    # kondr = grammar(n - 1, k)
    # for ch in kondr:
    #     if ch == '0':
    #         nxt.append('01')
    #     elif ch == '1':
    #         nxt.append('10')
    # return ''.join(nxt)


def main():
    n = int(input())
    k = int(input())

    # kond = grammar(n, k)
    # print(kond)

    # print(n, len(kondr), kondr)
    # print(kondr[k-1])


    # el = ''
    # for i in range(2**n):
    #     el += str(grammar(n, i))
    # print('0110100110010110', '0110100110010110'[k-1])
    # print(el, el[k-1])
    print(grammar(n, k-1))


def main_input():
    with open(r'input.txt', 'r') as f:
        n = int(f.readline())
        k = int(f.readline())

        print(grammar(n, k)[k-1])


if __name__ == "__main__":
    main()

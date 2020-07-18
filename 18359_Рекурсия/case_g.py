
def alph(ch):
    if ch > 'a':
        alph(chr(ord(ch) - 1))
        print(ch, end=' ')
        return

    print('a', end=' ')


def main():
    ch = input()

    alph(ch)


def main_input():
    with open('input.txt', 'r') as f:
        ch = f.read()

        alph(ch)


if __name__ == "__main__":
    main_input()

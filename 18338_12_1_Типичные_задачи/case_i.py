def main():
    a = input()
    b = input()
    result = []
    mind = 0
    if (len(b) > len(a)):
        a, b = b, a

    for i in range(len(a)):

        val = ord(a[-i-1]) - ord('0') + mind
        if i < len(b):
            val = val + ord(b[-i-1]) - ord('0')

        result.append(chr((val & 1) + ord('0')))
        mind = val >> 1

    while(mind > 0):
        result.append(chr((mind & 1) + ord('0')))
        mind = mind >> 1

    print("".join(reversed(result)))


if __name__ == "__main__":
    main()

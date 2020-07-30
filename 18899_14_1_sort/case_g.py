# echo "4\n6 3 3 2 "| python case_g.py
# echo "6\n5 3 7 2 8 3"| python case_g.py
def main():
    _ = input()
    # arr = list(map(int, input().split()))
    arr = [int(x) for x in input().split()]
    arr.sort()
    max_p = 0
    a = 0
    b, c = arr[:2]
    for el in arr[2:]:
        a, b, c = b, c, el
        if c < a + b:
            p = a + b + c
            if p > max_p:
                max_p = p
    print(max_p)


if __name__ == "__main__":
    main()

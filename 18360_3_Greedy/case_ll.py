def stair(arr):

    cur = arr[0]
    for el in arr:
        cur = max(el, cur-1)
        if cur == 0:
            return False

    return True


def main():
    n = int(input())
    arr = list(map(int, input().split()))

    print(stair(arr))


if __name__ == "__main__":
    main()

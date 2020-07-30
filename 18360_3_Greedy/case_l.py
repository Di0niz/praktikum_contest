def is_slice(arr, n):

    target = sum(arr)
    if target % 2 != 0:
        return False

    target = target // 2
    i, j = 0, n - 1
    arr = sorted(arr)
    while (i < j and target > 0):
        if arr[j] <= target:
            target -= arr[j]
            j -= 1
        # elif arr[i] <= target:
        #     target -= arr[i]
        #     i += 1
        # если не получилось пройти вперед
        # выкидываем предыдущий большой элемент
        elif j < n - 1:
            target += arr[j+1]

    return target == 0


def main():
    n = int(input())
    arr = list(map(int, input().split()))

    result = is_slice(arr, n)

    print(result)


if __name__ == "__main__":
    main()

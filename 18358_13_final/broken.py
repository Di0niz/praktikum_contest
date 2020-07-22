n = int(input())
x = int(input())


arr = list(map(int, input().split()))
broken = 0

for i, el in enumerate(arr[1:], start=1):
    if el < arr[i - 1]:
        broken = i

def binarySearch(arr, x, l, r):
    if r < l:
        return -1

    mid = l + (r - l) // 2
    arr_mid = arr[(mid + broken) % len(arr)]

    if arr_mid == x:
        return (mid + broken) % len(arr)
    elif arr_mid > x:
        return binarySearch(arr, x, l, mid - 1)

    return binarySearch(arr, x, mid + 1, r)


print(binarySearch(arr, x, 0, len(arr)))

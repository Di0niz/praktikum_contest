
# echo "3\n5\n4 9 5\n9 4 9 8 4" | python case_d.py
# echo "3\n8\n7 8 10\n9 7 5 3 6 6 4 1" | python case_d.py


def main():
    n = int(input())
    m = int(input())

    arr_n = list(map(int, input().split())) if n > 0 else []
    arr_m = set(map(int, input().split())) if m > 0 else []

    i, j = 0, 0

    views = set()
    for t in arr_n:
        if t in arr_m and not (t in views):
            print(t, end=" ")
            views.add(t)


if __name__ == "__main__":
    main()

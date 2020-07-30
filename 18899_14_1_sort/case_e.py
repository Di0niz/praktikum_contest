
# echo "5\n7\n4 9 5 2 2\n9 4 9 8 4 2 2" | python case_e.py

def main():
    n = int(input())
    m = int(input())

    arr_n = list(map(int, input().split())) if n > 0 else []
    arr_m = list(map(int, input().split())) if m > 0 else []

    race = dict()
    for t in arr_m:
        if t in race:
            race[t] += 1
        else:
            race[t] = 1

    for t in arr_n:
        if t in race and race[t] > 0:
            print(t, end=" ")
            race[t] -= 1


if __name__ == "__main__":
    main()



def main():
    n = int(input())

    times = []
    for _ in range(n):
        times.append([float(x) for x in input().split()])

    times = sorted(times, key=lambda key: (key[1], 1/(key[1]-key[0] + 1)))

    candidates = [times.pop(0)]

    for t in times:
        last = candidates[-1]
        if last[1] <= t[0]:
            candidates.append(t)

    print(len(candidates))
    for cand in candidates:
        print("%d %d" % (cand[0], cand[1]))


if __name__ == "__main__":
    main()

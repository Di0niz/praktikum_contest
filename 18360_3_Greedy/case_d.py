

def main():
    capacity = int(input())
    n = int(input())
    items = [
        [int(x) for x in input().split()] + [i] for i in range(n)
    ]

    items = sorted(items, key=lambda v: (-v[0], v[1], v[2]))
price_density.sort(key=lambda v: (-v[0], v[1], v[2]))

    result = []

    for _, weight, index in items:
        if capacity >= weight:
            result.append(index)
            capacity -= weight

    print(" ".join((str(x) for x in sorted(result))))


if __name__ == "__main__":
    main()

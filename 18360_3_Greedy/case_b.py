

def main():
    n = int(input())
    rates = [int(x) for x in input().split()]

    deals = []
    for i in range(1, n):
        if rates[i] > rates[i-1]:
            deals.append(rates[i] - rates[i-1])

    print(sum(deals))


if __name__ == "__main__":
    main()


def solution(k, fund):

    if k > 0:
        if sum(fund) % k != 0:
            return False

        amount = sum(fund) // k
        while amount:
            # ищем минмак элементы
            max_val = max(fund)
            min_val = min(fund)
            if amount >= max_val:
                amount -= max_val
                # выкидываем уже обработанный
                fund.pop(fund.index(max_val))
            if amount >= min_val:
                amount -= min_val
                fund.pop(fund.index(min_val))
            else:
                # если не удалось вставить самый маленький
                break

        if amount != 0:
            return False

        return solution(k-1, fund)
    elif k == 0 and fund == []:
        return True

    return False


def main():

    with open('input.txt', 'r') as f:
        k = int(f.readline())
        n = int(f.readline())
        fund = [int(x) for x in f.readline().split()]
        print(solution(k, fund))


if __name__ == "__main__":
    main()

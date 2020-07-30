k = 2
n = 7
L = [10, 7, 5, 4, 3, 1]
# k = 2
# n = 7
# L = [2, 3, 1, 3, 5, 2, 1]


def solution(k, fund):

    print(k, fund)
    if k > 0:
        if sum(fund) % k != 0:
            return False
        amount = sum(fund) // k
        while amount:
            print(fund)

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

            print(fund)
        if amount != 0:
            return False
        return solution(k-1, fund)
    elif k == 0 and fund == []:
        return True
    return False


print(solution(k, L))

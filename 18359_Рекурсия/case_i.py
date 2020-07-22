k = 4
n = 7
L = [4, 3, 2, 3, 5, 2, 1]
# k = 2
# n = 7
# L = [2, 3, 1, 3, 5, 2, 1]


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


print(solution(k, L))

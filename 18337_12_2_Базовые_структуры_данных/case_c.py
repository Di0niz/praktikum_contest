
def main():

    # читаем данные
    line = input()

    # массив для подсчетов
    counter = [0] * len(line)
    # массив текущей последовательность
    res = []

    # заполняем начальными значениями
    res.append(line[0])
    counter = 1
    max_counter = 1

    for i, ch in enumerate(line[1:], 1):
        if ch in res:
            # ищем позицию встреченного элемента
            pos = res.index(ch)
            res = res[pos+1:]
            counter -= pos
        else:
            counter += 1

        # добавляем новую букву в последовательность
        res.append(ch)

        max_counter = max(counter, max_counter)

    # выводим максимальную последовательность
    print(max_counter)


if __name__ == "__main__":
    main()

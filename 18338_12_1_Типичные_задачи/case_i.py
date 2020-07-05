def main():
    a = input()
    b = input()
    result = []
    mind = 0
    if (len(b) > len(a)):
        a, b = b, a

    for i in range(len(a)):

        # выполнять в циклах ord('1') плохая идея, лучше заменить на константу

        # заменяем ord('1') на 1
        # заменяем ord('0') на 0
        val = (1 if a[-i-1] == '1' else 0) + mind
        if i < len(b):
            val = val + (1 if b[-i-1] == '1' else 0)

        # строковая операция объединения тяжелая 
        # result = chr(val + ord('48')) + result

        # заменено на использование массива
        # возможно улучшение перфоманса, отказом от массива и переход на битовую маску
        result.append(val & 1)
        mind = val >> 1

    while(mind > 0):
        result.append(mind)
        mind = mind >> 1

    # заменяем ord('0') на 48
    print("".join((chr(x + 48) for x in result[::-1])))


if __name__ == "__main__":
    main()

def zero(arr):
    return sum((val != 0 for val in arr)) == 0


secure = input()
template = input()

# расчитываем маску для подсчетов
mask = {}
for t in template:
    mask[t] = mask.get(t, 0) + 1
# расчитываем контрольную сумму маски
mask_crc = sum([ord(ch) for ch in template])

found = 0

# запоминаем длину шаблона
len_template = len(template)

# расчитываем первое окно (-1 символ, так как в цикле добавил)
window = [ch for ch in secure[0:len_template-1]]
crc = sum([ord(ch) for ch in window])

i = len_template-1
while i < len(secure):
    # текущий символ
    ch = secure[i]
    # добавляем символ
    window.append(ch)
    crc = crc + ord(ch)

    # тогда и только, когда совпала контрольная сумма
    if crc == mask_crc:
        # считаем для похожей последовательности
        anagram = mask.copy()
        for t in window:
            anagram[t] = anagram.get(t, 0) - 1
        if zero(anagram.values()):
            found += 1

    # двигаем окно, выталкиваем один элемент
    pop_ch = window.pop(0)
    # перерасчитываем контрольную сумму
    crc = crc - ord(pop_ch)

    i += 1

print(found)

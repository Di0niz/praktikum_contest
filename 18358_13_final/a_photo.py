n = int(input())
L = list(map(int, input().split()))

photo = 0

while len(L) >= 2:

    max_el, min_el = max(L), min(L)
    photo += 1

    for el in (max_el, min_el,):
        i = L.index(el)
        L[i] -= 1
        if L[i] == 0:
            L.pop(i)

    print(L)

print(photo)

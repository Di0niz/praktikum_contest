n = int(input())
L = {}
for _ in range(n):
    st = input()
    h = hash(st)
    if not (h in L):
        print(st)
        L[h] = 1

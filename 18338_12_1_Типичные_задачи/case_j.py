from functools import reduce


n = int(input())

workers = (
    int(x) for x in input().split()
)

# решение через XOR
super_worker = reduce((lambda x, y: x ^ y), workers)


print(super_worker)

# n = int(input())
# workers = (
#     int(x) for x in input().split()
# )



# # XOR
# counters = [0] * 10000

# # считаем
# for i in workers:
#     counters[i] += 1

# # ищем
# super_worker = [
#     worker
#     for worker in range(len(counters))
#     if counters[worker] % 2 > 0  # ищем нечетных сотрудников
# ].pop()

# print(super_worker)

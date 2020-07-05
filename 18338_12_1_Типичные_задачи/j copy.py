# n = int(input())
# workers = (
#     int(x) for x in input().split()
# )
# # используем словарик для подсчетов (компактнее)
# counters = dict()

# # считаем
# for worker in workers:
#     counters[worker] = counters.get(worker, 0) + 1

# # ищем
# super_worker = list(
#         filter(lambda x: counters[x] % 2 > 0, counters)
#     ).pop()

# print(super_worker)

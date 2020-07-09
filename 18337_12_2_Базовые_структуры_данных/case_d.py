n, m = int(input()), int(input())
neib = [
    input().split() for _ in range(n)
]

tx, ty = int(input()), int(input())

dirs = (
    (x + tx, y + ty)
    for x, y in ((0, 1), (0, -1), (1, 0), (-1, 0))
    if x + tx >= 0 and x + tx < n and y + ty >= 0 and y + ty < m
)

results = sorted((neib[x][y] for x, y in dirs), key=lambda val: int(val))

print(' '.join(results))

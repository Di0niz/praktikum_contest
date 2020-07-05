

# норм
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# считываем данные
w = int(input())
head = None
for j in range(w):
    # сразу разворачиваем
    head = Node(input(), head)

# выводим сформированный список
cur = head
while cur:
    print(cur.value)
    cur = cur.next

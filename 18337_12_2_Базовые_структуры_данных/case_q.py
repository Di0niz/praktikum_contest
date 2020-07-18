class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.arr = [0] * max_size
        self.tail = 0
        self.head = 0

    def size(self):
        return self.size

    def push_back(self, value):
        if self.size == self.max_size:
            return None
        self.arr[self.head] = value
        self.head = (self.head + 1) % self.max_size
        self.size += 1
        return True

    def push_front(self, value):
        if self.size == self.max_size:
            return None
        self.tail = (self.tail - 1) % self.max_size
        self.size += 1
        self.arr[self.tail] = value
        return True

    def pop_front(self):
        if self.size == 0:
            return None

        val = self.arr[self.tail]
        self.arr[self.tail] = 0
        self.tail = (self.tail + 1) % self.max_size
        self.size -= 1
        return val

    def pop_back(self):
        if self.size == 0:
            return None

        self.head = (self.head - 1) % self.max_size
        val = self.arr[self.head]
        self.arr[self.head] = 0

        self.size -= 1
        return val


def main():

    n = int(input())
    m = int(input())

    q = Queue(m)

    for _ in range(n):
        cmd = input().split()
        if cmd[0] == 'push_back':
            if not q.push_back(cmd[1]):
                print("error")
        elif cmd[0] == 'push_front':
            if not q.push_front(cmd[1]):
                print("error")
        elif cmd[0] == 'pop_front':
            val = q.pop_front()
            print("error" if val is None else val)
        elif cmd[0] == 'pop_back':
            val = q.pop_back()
            print("error" if val is None else val)
        elif cmd[0] == 'size':
            val = q.size()
            print("error" if val is None else val)


if __name__ == "__main__":
    main()

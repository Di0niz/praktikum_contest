class UniqStack:
    
    def __init__(self):
        self.stack = []
        self.uniq = set()
        self.count = 0

    def push(self, val):
        if not (val in self.uniq):
            self.uniq.add(val)
            self.stack.append(val)
            self.count += 1

    def peek(self):
        if self.count > 0:
            return self.stack[-1]
        return None

    def pop(self):
        v = None
        if self.count > 0:
            v = self.stack.pop()
            self.uniq.remove(v)
            self.count -= 1
        return v

    def size(self):
        return self.count


def main():
    n = int(input())
    st = UniqStack()
    for _ in range(n):
        command = input()
        cc = command[:2]
        if cc == "pu":  # push
            _, val = command.split(' ')
            st.push(val)
        elif cc == "po":  # pop
            res = st.pop()
            if not res:
                print("error")
        elif cc == "pe":  # peek
            res = st.peek()
            if res:
                print(res)
            else:
                print("error")
        elif cc == "si":  # size
            print(st.size())


if __name__ == "__main__":
    main()

LEFT_BRACKETS = ('(', '[', '{')
RIGHT_BRACKETS = (')', ']', '}')


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if item in LEFT_BRACKETS:
            self.items.append(item)

    def pop(self):
        return self.items.pop()


brackets_stack = Stack()

result = True

for bracket in input():
    if bracket in LEFT_BRACKETS:
        brackets_stack.push(bracket)
    elif not brackets_stack.isEmpty():
        
        left_bracket = brackets_stack.pop()
        right_bracket = RIGHT_BRACKETS[LEFT_BRACKETS.index(left_bracket)]

        if right_bracket != bracket:
            result = False
            break
    else:
        result = False
        break

print(result and brackets_stack.isEmpty())

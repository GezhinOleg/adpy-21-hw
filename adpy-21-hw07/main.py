BAL_DICT = {
    '(': ')',
    '[': ']',
    '{': '}'
}

BALLANCED_LIST = [
    '(((([{}]))))',
    '[([])((([[[]]])))]{()}',
    '{{[()]}}'
]
UNBALLANCED_LIST = [
    '}{}',
    '{{[(])]}}',
    '[[{())}]'
]


class Stack(list):
    def isEmpty(self):
        return len(self) == 0

    def push(self, _item):
        self.append(_item)

    def pop(self):
        if not self.isEmpty():
            _item = self[-1]
            self.__delitem__(-1)
            return _item

    def peek(self):
        if not self.isEmpty():
            return self[-1]


def check_ballance(seq_):
    stack = Stack()
    ballanced = True
    for item_ in seq_:
        if item_ in BAL_DICT:
            stack.push(item_)
        elif item_ == BAL_DICT.get(stack.peek()):
            stack.pop()
        else:
            return False
    return ballanced & stack.isEmpty()


if __name__ == '__main__':
    for seq in BALLANCED_LIST:
        print(check_ballance(seq))
    for seq in UNBALLANCED_LIST:
        print(check_ballance(seq))
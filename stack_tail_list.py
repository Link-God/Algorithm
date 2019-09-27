from sys import stdin


class Node:
    def __init__(self, node):
        self.node = node
        self.prev = None


class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.tail = Node(None)
        self.length = 0

    def push(self, node):
        if self.length == self.max_size:
            return 'overflow\n'
        if not self.tail.node:
            self.tail = Node(node)
            self.length += 1
        else:
            temp = self.tail
            self.tail = Node(node)
            self.tail.prev = temp
            self.length += 1
        return ''

    def print(self):
        temp = self.tail
        list_to_print = []
        while temp:
            list_to_print.append(temp.node)
            temp = temp.prev
        return ' '.join(str(x) for x in list_to_print[::-1]) + '\n'

    def pop(self):
        if self.length == 0:
            return 'underflow\n'
        temp = self.tail.node
        if self.tail.prev is not None:
            self.tail = self.tail.prev
        else:
            self.tail = Node(None)
        self.length -= 1
        return str(temp) + '\n'

    def __len__(self):
        return self.length


final_line = ''
for line in stdin:
    if 'set_size' in line:
        s = Stack(int(line[9::]))
        # s = Stack(line[9:].rstrip())
    elif 'pop' in line:
        final_line += s.pop()
    elif 'push' in line:
        # final_line += s.push(int(line[5:]))
        final_line += s.push(line[5:].rstrip())
    elif 'print' in line:
        final_line += s.print()
        print()

print(final_line)

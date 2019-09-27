from sys import stdin


class Node:
    def __init__(self, node):
        self.node = node
        self.next = None


class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.head = Node(None)
        self.tail = Node(None)
        self.length = 0

    def push(self, node):
        if self.length == self.max_size:
            return 'overflow\n'
        if not self.head.node:
            self.head = Node(node)
            self.tail = self.head
            self.length += 1
        else:
            self.tail.next = Node(node)
            self.tail = self.tail.next
            self.length += 1
        return ''

    def print(self):
        temp = self.head
        list_to_print = []
        while temp:
            list_to_print.append(temp.node)
            temp = temp.next
        return ' '.join(str(x) for x in list_to_print) + '\n'

    def pop(self):
        if self.length == 0:
            return 'underflow\n'
        temp = self.head.node
        if self.head.next is not None:
            self.head = self.head.next
        else:
            self.head = Node(None)
        self.length -= 1
        return str(temp) + '\n'

    def __len__(self):
        return self.length


final_line = ''
for line in stdin:
    if 'set_size' in line:
        q = Queue(int(line[9::]))
        # s = Stack(line[9:].rstrip())
    elif 'pop' in line:
        final_line += q.pop()
    elif 'push' in line:
        # final_line += s.push(int(line[5:]))
        final_line += q.push(line[5:].rstrip())
    elif 'print' in line:
        final_line += q.print()

print(final_line)

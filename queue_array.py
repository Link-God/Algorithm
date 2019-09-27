from sys import stdin, argv
from enum import Enum


class StrType(Enum):
    PUSH = 1
    POP = 2
    PRINT = 3
    SET_SIZE = 4


class Queue:
    def __init__(self, size):
        # self.arr = array.array('i', [0] * size)
        self.arr = [0] * size
        self.max_size = size
        self.tail = 0
        self.head = 0
        self.full = False

    def push(self, el):
        if self.tail == self.head and self.full:
            return 'overflow\n'
        self.arr[self.tail] = el
        if self.tail == self.max_size - 1:
            self.tail = 0
        else:
            self.tail += 1
        if self.tail == self.head:
            self.full = True
        return ''

    def pop(self):
        if self.head == self.tail:
            if not self.full:
                return 'underflow\n'
        if self.full:
            self.full = False
        temp = self.arr[self.head]
        if self.head == self.max_size - 1:
            self.head = 0
        else:
            self.head += 1
        return str(temp) + '\n'

    def print(self):
        if self.head == self.tail and not self.full:
            return 'empty\n'
        r_str = ''
        temp_head = self.head
        if self.full:
            r_str += str(self.arr[temp_head]) + ' '
            temp_head += 1
        while temp_head != self.tail:
            r_str += str(self.arr[temp_head]) + ' '
            if temp_head == self.max_size - 1:
                temp_head = 0
            else:
                temp_head += 1
        return r_str.strip() + '\n'


def have_error(check_line: str, str_type: StrType):
    if str_type == StrType.POP:
        if check_line.replace('pop', '') != '\n':
            return True
        else:
            return False
    elif str_type == StrType.PUSH:
        if len(check_line.replace('push', '').strip().split(' ')) != 1:
            return True
        else:
            return False
    elif str_type == StrType.PRINT:
        if check_line.replace('print', '') != '\n':
            return True
        else:
            return False
    elif str_type == StrType.SET_SIZE:
        if len(check_line.replace('set_size', '').strip().split(' ')) != 1:
            return True
        else:
            return False


q = None
final_line = ''
in_file, out_file = argv[1], argv[2]
with open(in_file, 'r') as file:
    for line in file:
        if line == '\n':
            continue

        if 'set_size' in line:
            if q is None:
                if have_error(line, StrType.SET_SIZE):
                    final_line += 'error\n'
                else:
                    q = Queue(int(line[9::]))
            else:
                final_line += 'error\n'

        elif 'pop' in line:
            if q:
                if have_error(line, StrType.POP):
                    final_line += 'error\n'
                else:
                    final_line += q.pop()
            else:
                final_line += 'error\n'

        elif 'push' in line:
            if q:
                if have_error(line, StrType.PUSH):
                    final_line += 'error\n'
                else:
                    final_line += q.push(line[5:].rstrip())
            else:
                final_line += 'error\n'

        elif 'print' in line:
            if q:
                if have_error(line, StrType.PRINT):
                    final_line += 'error\n'
                else:
                    final_line += q.print()
            else:
                final_line += 'error\n'
        else:
            final_line += 'error\n'

# print(final_line, end='')

with open(out_file, 'w') as file:
    file.write(final_line)

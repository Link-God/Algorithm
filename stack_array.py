# import array
from sys import stdin
from enum import Enum


class StrType(Enum):
    PUSH = 1
    POP = 2
    PRINT = 3
    SET_SIZE = 4


class Stack:
    def __init__(self, size):
        # self.arr = array.array('i', [0] * size)
        self.arr = [None] * size
        self.max_size = size
        self.tail = 0

    def push(self, el):
        if self.tail == self.max_size:
            return 'overflow\n'
        else:
            self.arr[self.tail] = el
            self.tail += 1
            return ''

    def pop(self):
        if self.tail == 0:
            return 'underflow\n'
        else:
            self.tail -= 1
            return str(self.arr[self.tail]) + '\n'

    def print(self):
        if self.tail == 0:
            return 'empty\n'
        return ' '.join(str(self.arr[i]) for i in range(self.tail)) + '\n'


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


s = None
final_line = ''
for line in stdin:
    if line == '\n':
        continue

    if 'set_size' in line:
        if s is None:
            if have_error(line, StrType.SET_SIZE):
                final_line += 'error\n'
            else:
                s = Stack(int(line[9::]))
        else:
            final_line += 'error\n'

    elif 'pop' in line:
        if s:
            if have_error(line, StrType.POP):
                final_line += 'error\n'
            else:
                final_line += s.pop()
        else:
            final_line += 'error\n'

    elif 'push' in line:
        if s:
            if have_error(line, StrType.PUSH):
                final_line += 'error\n'
            else:
                final_line += s.push(line[5:].rstrip())
        else:
            final_line += 'error\n'

    elif 'print' in line:
        if s:
            if have_error(line, StrType.PRINT):
                final_line += 'error\n'
            else:
                final_line += s.print()
        else:
            final_line += 'error\n'
    else:
        final_line += 'error\n'

print(final_line, end='')

from math import log2, log
from sys import stdin
from enum import Enum


class StrType(Enum):
    ADD = 1
    SEARCH = 2
    PRINT = 3
    SET = 4


M = (1 << 31) - 1


def eratosthenes(n):
    sieve = list(range(n + 2))
    sieve[1] = 0  # без этой строки итоговый список будет содержать единицу
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return sieve


def get_prime_by_index(index):
    return list(filter(lambda x: x != 0, eratosthenes(int(1.5 * index * log(index)) + 1)))[index - 1]


def family_of_hash_functions(x, index, m):
    return (((index + 1) * x + get_prime_by_index(index + 1)) % M) % m


class BitArray:
    def __init__(self, size):
        self.bit_array = 0
        self.size = size

    def add(self, key):
        self.bit_array |= (1 << key)

    def find(self, key):
        if (self.bit_array & (1 << key)) == 0:
            return False
        return True

    def print(self):
        return bin(self.bit_array)[:1:-1] + '0' * (self.size - len(bin(self.bit_array)[2:]))


class BlumFilter:
    def __init__(self, n, P):
        self.size_of_array = round(-n * log2(P) / log(2))
        self.quantity_of_hash_func = round(-log2(P))
        self.bit_array = BitArray(self.size_of_array)
        self.hash_func = family_of_hash_functions

    def add(self, key):
        for i in range(self.quantity_of_hash_func):
            self.bit_array.add(self.hash_func(key, i, self.size_of_array))

    def search(self, key):
        for i in range(self.quantity_of_hash_func):
            if not self.bit_array.find(self.hash_func(key, i, self.size_of_array)):
                return False
        return True

    def print(self):
        return self.bit_array.print()


def have_error(check_line: str, str_type: StrType):
    if str_type == StrType.SEARCH:
        if len(check_line.replace('search', '').strip().split(' ')) != 1:
            return True
        else:
            return False
    elif str_type == StrType.ADD:
        if len(check_line.replace('add', '').strip().split(' ')) != 1:
            return True
        else:
            return False
    elif str_type == StrType.PRINT:
        if check_line.replace('print', '') != '\n':
            return True
        else:
            return False
    elif str_type == StrType.SET:
        if len(check_line.replace('set', '').strip().split(' ')) != 2:
            return True
        else:
            return False


if __name__ == "__main__":
    B_filter = None
    final_line = ''
    for line in stdin:
        if line == '\n':
            continue
        if 'set' in line:
            if B_filter is None:
                if have_error(line, StrType.SET):
                    final_line += 'error\n'
                else:
                    try:
                        B_filter = BlumFilter(*list(map(float, line[len('set'):].split())))
                        if B_filter.size_of_array <= 0 or B_filter.quantity_of_hash_func <= 0:
                            B_filter = None
                            raise ValueError
                        final_line += str(B_filter.size_of_array) + ' ' + str(B_filter.quantity_of_hash_func) + '\n'
                    except ValueError:
                        final_line += 'error\n'
            else:
                final_line += 'error\n'

        elif 'search' in line:
            if B_filter:
                if have_error(line, StrType.SEARCH):
                    final_line += 'error\n'
                else:
                    final_line += '1\n' if B_filter.search(int(line[len('search'):].strip())) else '0\n'
            else:
                final_line += 'error\n'

        elif 'add' in line:
            if B_filter:
                if have_error(line, StrType.ADD):
                    final_line += 'error\n'
                else:
                    B_filter.add(int(line[len('add'):].strip()))
            else:
                final_line += 'error\n'

        elif 'print' in line:
            if B_filter:
                if have_error(line, StrType.PRINT):
                    final_line += 'error\n'
                else:
                    final_line += B_filter.print() + '\n'
            else:
                final_line += 'error\n'
        else:
            final_line += 'error\n'

    print(final_line, end='')

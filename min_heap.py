from enum import Enum
from sys import stdin
from math import log2


class StrType(Enum):
    ADD = 1
    SEARCH = 2
    PRINT = 3
    SET = 4
    MAX = 5
    MIN = 6
    DELETE = 7
    EXTRACT = 8


class Node:
    def __init__(self, key, value, index, parent_key=None):
        self.key = key
        self.value = value
        self.index = index
        self.parent_key = parent_key

    def set(self, other):
        self.key = other.key
        self.value = other.value

    def swap_index(self, other):
        self.index, other.index = other.index, self.index

    def __repr__(self):
        return "key:{}, value:{}, index:{}".format(self.key, self.value, self.index)

    def __str__(self):
        if self.index == 0:
            return "[{} {}]".format(self.key, self.value)
        else:
            return ('\n' if log2(self.index + 1).is_integer() else ' ') + "[{} {} {}]".format(self.key, self.value,
                                                                                              self.parent_key)

    def __eq__(self, other):
        # ==
        if isinstance(other, Node) and self.key == other.key:
            return True
        else:
            return False

    def __ne__(self, other):
        # !=
        return not self.__eq__(other)

    def __lt__(self, other):
        # <
        if isinstance(other, Node) and self.key < other.key:
            return True
        else:
            return False

    def __gt__(self, other):
        # >
        if isinstance(other, Node) and self.key > other.key:
            return True
        else:
            return False

    def __le__(self, other):
        # <=
        if isinstance(other, Node) and self.key <= other.key:
            return True
        else:
            return False

    def __ge__(self, other):
        # >=
        if isinstance(other, Node) and self.key >= other.key:
            return True
        else:
            return False


class MinHeap:
    def __init__(self):
        self.array = []
        self.dict = {}
        self.max_element = None

    def _sift_down(self, index):
        while 2 * index + 1 < len(self.array):
            left_i = 2 * index + 1
            right_i = 2 * index + 2
            min_el = min(self.array[left_i], self.array[right_i]) if right_i < len(self.array) else self.array[left_i]
            self._swap_in_array(min_el.index, index)
            min_el.swap_index(index)

    def _sift_up(self, index):
        parent_index = (index - 1) // 2
        while self.array[index] > self.array[parent_index]:
            self._swap_in_array(index, parent_index)
            self.array[index].swap_index(self.array[parent_index])
            index = parent_index

    def _swap_in_array(self, index, parent_index):
        index_key = self.array[index].key
        parent_index_key = self.array[parent_index].key

        self.array[index].parent_key = parent_index_key
        self.array[parent_index].parent_key = index_key
        if index == 2 * parent_index + 1 and index + 1 < len(self.array):
            self.array[index + 1].parent_key = index_key
        else:
            self.array[index - 1].parent_ley = index_key

        # TODO дети node_index родитель не поменсля !!
        self.array[index], self.array[parent_index] = self.array[parent_index], self.array[index]

    def add(self, key, value):
        node = Node(key, value, len(self.array))
        parent_index = (node.index - 1) // 2
        if len(self.array) == 0:
            self.max_element = node
        else:
            self.max_element = max(self.max_element, node)
            node.parent_key = self.array[parent_index].key

        if self.dict.get(key):
            raise KeyError
        self.dict[key] = node
        self.array.append(node)

        while node.index > 0 and self.array[parent_index] > self.array[node.index]:
            parent = self.array[parent_index]
            self._swap_in_array(node.index, parent_index)
            node.swap_index(parent)

            parent_index = (node.index - 1) // 2

    def set(self, key, value):
        node = self.dict.get(key)
        if node:
            node.value = value
        else:
            raise KeyError

    def extend(self):
        pass

    def min(self):
        node = self.array[0]
        return node.key, 0, node.value

    def max(self):
        node = self.max_element
        return node.key, node.index, node.value

    def string_representation(self):
        high = int(log2(len(self.array)))
        list_to_print = self.array + [' _'] * (((1 << (high + 1)) - 1) - len(self.array))
        return ''.join(str(x) for x in list_to_print)

    def _search_node(self, key):
        return self.dict.get(key)

    def search(self, key):
        node = self._search_node(key)
        if node:
            return node.value
        else:
            return None

    def delete(self, key):
        node = self._search_node(key)
        if node is None:
            raise KeyError

        self.dict.pop(key)
        node.set(self.array.pop())
        if node.key < self.array[(node.index - 1) // 2]:
            self._sift_up(node.index)
        else:
            self._sift_down(node.index)


class Handler:
    def __init__(self, handler_object=stdin):
        self.handler_object = handler_object

    def parse(self):
        heap = MinHeap()
        final_line = ''
        for line in self.handler_object:
            if line == '\n':
                continue
            if line.find('set') == 0:
                if self.have_error(line, StrType.SET):
                    final_line += 'error\n'
                else:
                    pass

            elif line.find('search') == 0:
                if self.have_error(line, StrType.SEARCH):
                    final_line += 'error\n'
                else:
                    pass

            elif line.find('add') == 0:
                if self.have_error(line, StrType.ADD):
                    final_line += 'error\n'
                else:
                    pass

            elif line.find('print') == 0:
                if self.have_error(line, StrType.PRINT):
                    final_line += 'error\n'
                else:
                    pass

            elif line.find('max') == 0:
                if self.have_error(line, StrType.MAX):
                    final_line += 'error\n'
                else:
                    pass

            elif line.find('min') == 0:
                if self.have_error(line, StrType.MIN):
                    final_line += 'error\n'
                else:
                    pass

            elif line.find('delete') == 0:
                if self.have_error(line, StrType.DELETE):
                    final_line += 'error\n'
                else:
                    pass

            else:
                final_line += 'error\n'

        return final_line

    @staticmethod
    def have_error(check_line: str, str_type: StrType):
        if str_type == StrType.SEARCH:
            if len(check_line.replace('search', '').strip().split(' ')) != 1:
                return True
            else:
                return False
        elif str_type == StrType.EXTRACT:
            if check_line.replace('extract', '') != '\n':
                return True
            else:
                return False
        elif str_type == StrType.ADD:
            if len(check_line.replace('add', '').strip().split(' ')) != 2:
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
        elif str_type == StrType.MAX:
            if check_line.replace('max', '') != '\n':
                return True
            else:
                return False
        elif str_type == StrType.MIN:
            if check_line.replace('min', '') != '\n':
                return True
            else:
                return False
        elif str_type == StrType.DELETE:
            if len(check_line.replace('delete', '').strip().split(' ')) != 1:
                return True
            else:
                return False


if __name__ == "__main__":
    h = MinHeap()
    h.add(1, 2)
    h.add(2, 1)
    h.add(3, 4)
    h.add(0, 4)

    h.add(5, 4)
    h.add(6, 4)
    h.add(7, 4)
    h.add(8, 4)
    h.set(2, 10)
    # h.delete(2)
    print(h.string_representation())
    # handler = Handler()
    # final_string = handler.parse()
    # print(final_string, end='\n')

from enum import Enum
from sys import stdin


class StrType(Enum):
    ADD = 1
    SEARCH = 2
    PRINT = 3
    SET = 4
    MAX = 5
    MIN = 6
    DELETE = 7


class Node:
    def __init__(self, key, value, parent=None, left_ch=None, right_ch=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.right_child = right_ch
        self.left_child = left_ch

    def __bool__(self):
        return bool((self.key is not None) and (self.value is not None))


class EmptyTree(Exception):
    def __init__(self, message=None):
        super().__init__(message)


class BST:
    def __init__(self):
        self.root = Node(None, None)

    def _add_note(self, key, value):
        node = Node(key, value)
        parent = None
        temp = self.root
        while temp:
            parent = temp
            if key < temp.key:
                temp = temp.left_child
            else:
                temp = temp.right_child
        node.parent = parent
        if parent is None:
            self.root = node
        elif key < parent.key:
            parent.left_child = node
        elif key > parent.key:
            parent.right_child = node
        else:
            raise KeyError
        return node

    def add(self, key, value):
        _ = self._add_note(key, value)

    def _search_node(self, key):
        temp = self.root
        while temp:
            if temp.key == key:
                return temp
            else:
                if temp.key > key:
                    if not temp.left_child:
                        break
                    temp = temp.left_child
                else:
                    if not temp.right_child:
                        break
                    temp = temp.right_child
        return temp

    def search(self, key):
        node = self._search_node(key)
        if node and node.key == key:
            return True
        else:
            return False

    def _set_node(self, key, value):
        node = self._search_node(key)
        if node.key == key:
            node.value = value
            return node

    def set(self, key, value):
        """
        :return:True if success , else False
        """
        node = self._search_node(key)
        if node:
            node.value = value
        else:
            raise KeyError

    def _min_node(self, root=None):
        temp = self.root if not root else root
        while temp.left_child:
            temp = temp.left_child
        return temp

    def _max_node(self, root=None):
        temp = self.root if not root else root
        while temp.right_child:
            temp = temp.right_child
        return temp

    def min(self):
        node = self._min_node()
        if node:
            return node.key, node.value
        else:
            raise EmptyTree

    def max(self):
        node = self._max_node()
        if node:
            return node.key, node.value
        else:
            raise EmptyTree

    def _previous_node(self, node: Node):
        if node.left_child is not None:
            return self._max_node(node.left_child)
        else:
            temp = node.parent
            while temp and node == temp.left_child:
                node = temp
                temp = temp.parent
            return temp

    def _next_node(self, node: Node):
        if node.right_child is not None:
            return self._max_node(node.right_child)
        else:
            temp = node.parent
            while temp and node == temp.right_child:
                node = temp
                temp = temp.parent
            return temp

    def delete(self, key):
        node = self._search_node(key)
        if not node:
            raise EmptyTree
        parent = node.parent
        if node.right_child is None and node.right_child is None:
            if parent.left_child == node:
                parent.left_child = None
            else:
                parent.right_child = None
        elif node.right_child is None or node.right_child is None:
            if node.left_child is None:
                if parent.left_child == node:
                    parent.left_child = node.right_child
                else:
                    parent.right_child = node.right_child
                node.right_child.parent = parent
            else:
                if parent.left_child == node:
                    parent.left_child = node.left_child
                else:
                    parent.right_child = node.left_child
                node.left_child.parent = parent
        else:
            p_node = self._previous_node(node)
            node.key, node.value = p_node.key, p_node.value
            if p_node.parent.left_child == p_node:
                p_node.parent.left_child = p_node.right_child
                if p_node.right_child is not None:
                    p_node.right_child.parent = p_node.parent
            else:
                p_node.parent.right_child = p_node.left_child
                if p_node.left_child is not None:
                    p_node.right_child.parent = p_node.parent


class SplayTree(BST):
    def __init__(self):
        super().__init__()
        self.size = 0

    def _rotate_right(self, node: Node):
        left_ch = node.left_child
        node.left_child = left_ch.right_child
        if left_ch.right_child is not None:
            left_ch.right_child.parent = node

        left_ch.parent = node.parent
        if node.parent is None:
            self.root = left_ch
        elif node == node.parent.right_child:
            node.parent.right_child = left_ch
        else:
            node.parent.left_child = left_ch

        left_ch.right_child = node
        node.parent = left_ch

    def _rotate_left(self, node: Node):
        right_ch = node.right_child
        node.right_child = right_ch.left_child
        if right_ch.left_child is not None:
            right_ch.left_child.parent = node

        right_ch.parent = node.parent
        if node.parent is None:
            self.root = right_ch
        elif node == node.parent.left_child:
            node.parent.left_child = right_ch
        else:
            node.parent.right_child = right_ch
        right_ch.left_child = node
        node.parent = right_ch

    def _zig(self, node: Node):
        self._rotate_right(node.parent)

    def _zag(self, node: Node):
        self._rotate_left(node.parent)

    def _zig_zig(self, node: Node):
        self._rotate_right(node.parent.parent)
        self._rotate_right(node.parent)

    def _zag_zag(self, node: Node):
        self._rotate_left(node.parent.parent)
        self._rotate_left(node.parent)

    def _zig_zag(self, node: Node):
        self._rotate_left(node.parent)
        self._rotate_right(node.parent)

    def _zag_zig(self, node: Node):
        self._rotate_right(node.parent)
        self._rotate_left(node.parent)

    def _splay(self, node: Node):
        while node.parent is not None:
            if node.parent.parent is None:
                if node == node.parent.left_child:
                    self._zig(node)
                else:
                    self._zag(node)
            elif node == node.parent.left_child and node.parent == node.parent.parent.left_child:
                self._zig_zig(node)

            elif node == node.parent.right_child and node.parent == node.parent.parent.right_child:
                self._zag_zag(node)
            elif node == node.parent.right_child and node.parent == node.parent.parent.left_child:
                self._zig_zag(node)
            elif node == node.parent.left_child and node.parent == node.parent.parent.right_child:
                self._zag_zig(node)

    def add(self, key, value):
        node = self._add_note(key, value)
        self.size += 1
        self._splay(node)

    def search(self, key):
        node = self._search_node(key)
        if node and node.key == key:
            self._splay(node)
            return node.value
        else:
            self._splay(node)
            return None

    def set(self, key, value):
        node = self._set_node(key, value)
        if node:
            self._splay(node)
        else:
            raise KeyError

    def delete(self, key):
        node = self._search_node(key)
        if node.key == key:
            self.size -= 1
            self._splay(node)
            if self.root.left_child is not None and self.root.right_child is not None:
                L_tree = SplayTree()
                R_tree = SplayTree()

                self.root.left_child.parent = None
                L_tree.root = self.root.left_child
                R_tree.root = self.root.right_child

                L_tree.max()
                self.root = L_tree.root
                self.root.right_child = R_tree.root
                self.root.right_child.parent = self.root

            elif self.root.left_child is not None:
                self.root.left_child.parent = None
                self.root = self.root.left_child
            elif self.root.right_child is not None:
                self.root.right_child.parent = None
                self.root = self.root.right_child
            else:
                self.root = Node(None, None)
        else:
            raise KeyError

    def min(self):
        node = self._min_node()
        if node:
            self._splay(node)
            return node.key, node.value
        else:
            raise EmptyTree

    def max(self):
        node = self._max_node()
        if node:
            self._splay(node)
            return node.key, node.value
        else:
            raise EmptyTree

    def p_node(self, n: Node):
        if n == self.root:
            return '[' + str(n.key) + ' ' + str(n.value) + ']'
        else:
            return '[' + str(n.key) + ' ' + str(n.value) + ' ' + str(n.parent.key) + ']'

    def find_high_and_indexes(self, node, h, index, dict_of_indexes: dict):
        if node:
            new_h = h + 1
            left_index = 2 * index + 1
            right_index = 2 * index + 2
            dict_of_indexes[index] = node

            return max(self.find_high_and_indexes(node.left_child, new_h, left_index, dict_of_indexes),
                       self.find_high_and_indexes(node.right_child, new_h, right_index, dict_of_indexes))
        else:
            return h

    def string_representation(self):
        dict_of_indexes = {}
        high = self.find_high_and_indexes(self.root, 0, 0, dict_of_indexes)
        need_to_print = (1 << high) - 1

        if need_to_print == 0:
            return '_'

        list_of_nodes = [' _'] * need_to_print

        for index, node in dict_of_indexes.items():
            if ((index + 1) & index) == 0:
                list_of_nodes[index] = ('\n' if index != 0 else '') + self.p_node(node)
            else:
                list_of_nodes[index] = ' ' + self.p_node(node)
        for i in range(1, high):
            index = 2 ** i
            list_of_nodes[index - 1] = '\n' + list_of_nodes[index - 1][1:]

        string = ''.join(list_of_nodes)
        return string.strip()


class Handler:
    def __init__(self, handler_object=stdin):
        self.handler_object = handler_object

    def parse(self):
        S_tree = SplayTree()
        final_line = ''
        for line in self.handler_object:
            if line == '\n':
                continue
            if line.find('set') == 0:
                if self.have_error(line, StrType.SET):
                    final_line += 'error\n'
                else:
                    try:
                        temp_list = line.replace('set', '').strip().split(' ')
                        key, value = int(temp_list[0]), str(temp_list[1])
                        S_tree.set(key, value)
                    except KeyError:
                        final_line += 'error\n'

            elif line.find('search') == 0:
                if self.have_error(line, StrType.SEARCH):
                    final_line += 'error\n'
                else:
                    key = int(line[len('search'):].strip())
                    value = S_tree.search(key)
                    final_line += '1 ' + str(value) + '\n' if value else '0\n'

            elif line.find('add') == 0:
                if self.have_error(line, StrType.ADD):
                    final_line += 'error\n'
                else:
                    try:
                        temp_list = line.replace('add', '').strip().split(' ')
                        key, value = int(temp_list[0]), str(temp_list[1])
                        S_tree.add(key, value)
                    except KeyError:
                        final_line += 'error\n'

            elif line.find('print') == 0:
                if self.have_error(line, StrType.PRINT):
                    final_line += 'error\n'
                else:
                    final_line += S_tree.string_representation() + '\n'

            elif line.find('max') == 0:
                if self.have_error(line, StrType.MAX):
                    final_line += 'error\n'
                else:
                    try:
                        final_line += '{} {}'.format(*S_tree.max()) + '\n'
                    except EmptyTree:
                        final_line += 'error\n'

            elif line.find('min') == 0:
                if self.have_error(line, StrType.MIN):
                    final_line += 'error\n'
                else:
                    try:
                        final_line += "{} {}".format(*S_tree.min()) + '\n'
                    except EmptyTree:
                        final_line += 'error\n'

            elif line.find('delete') == 0:
                if self.have_error(line, StrType.DELETE):
                    final_line += 'error\n'
                else:
                    try:
                        S_tree.delete(int(line[len('delete'):].strip()))
                    except KeyError:
                        final_line += 'error\n'

            else:
                final_line += 'error\n'

        print(final_line, end='')

    @staticmethod
    def have_error(check_line: str, str_type: StrType):
        if str_type == StrType.SEARCH:
            if len(check_line.replace('search', '').strip().split(' ')) != 1:
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
    handler = Handler()
    handler.parse()

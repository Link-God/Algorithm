from enum import Enum
from collections import deque


class StrType(Enum):
    ADD = 1
    SEARCH = 2
    PRINT = 3
    SET = 4


class Node:
    def __init__(self, key, value, parent=None, left_ch=None, right_ch=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.right_child = right_ch
        self.left_child = left_ch


class BST:
    root: Node

    def __init__(self):
        self.root = Node(None, None)

    def _add_note(self, key, value):
        node = Node(key, value)
        parent = None
        temp = self.root
        while temp and temp.key:
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
        else:
            parent.right_child = node
        return node

    def add(self, key, value):
        node = Node(key, value)
        parent = None
        temp = self.root
        while temp and temp.key:
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
        else:
            parent.right_child = node

    def _search_node(self, key):
        temp = self.root
        while temp.key:
            if temp.key == key:
                return temp
            else:
                if temp.key > key:
                    temp = temp.left_child
                else:
                    temp = temp.right_child
        return temp

    def search(self, key):
        node = self._search_node(key)
        if node.key == key:
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
        if node is not None:
            node.value = value
            return True
        else:
            return False

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
        return node.key, node.value

    def max(self):
        node = self._max_node()
        return node.key, node.value

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
        self.size += 1
        node = self._add_note(key, value)
        self._splay(node)

    def search(self, key):
        node = self._search_node(key)
        if node.key == key:
            self._splay(node)
            return node.value
        else:
            self._splay(node)
            return None

    def set(self, key, value):
        node = self._set_node(key, value)
        if node is not None:
            self._splay(node)
        else:
            raise KeyError

    def min(self):
        node = self._min_node()
        self._splay(node)
        return node.key, node.value

    def delete(self, key):
        node = self._search_node(key)
        if node.key == key:
            self.size -= 1
            self._splay(node)
            if self.root.left_child is not None:
                self.root.left_child.parent = None
                temp = self.root.left_child
                while temp and temp.right_child:
                    temp = temp.right_child
                self._splay(temp)
                self.root.left_child.right_child = self.root.right_child
                self.root.right_child.parent = self.root.left_child
                self.root = self.root.left_child
            else:
                self.root = self.root.right_child
        else:
            raise KeyError

    def max(self):
        node = self._max_node()
        self._splay(node)
        return node.key, node.value

    def string_representation(self):
        string = ''

        def p_node(n: Node):
            if n == self.root:
                return f"[{n.key} {n.value}]"
            else:
                return f"[{n.key} {n.value} {n.parent.key}]" if n is not None else '_'

        num_of_printed = 0
        num_of_printed_nodes = 0
        q = deque()
        q.append(self.root)
        while num_of_printed_nodes != self.size:
            num_of_printed += 1
            node = q.popleft()
            string += (p_node(node) + ('\n' if ((num_of_printed + 1) & num_of_printed == 0) else ' '))
            if node:
                num_of_printed_nodes += 1
                q.extend((node.left_child, node.right_child))
            else:
                q.extend((None, None))

        remaining_empties = ((1 << (len(bin(num_of_printed)[2:]))) - num_of_printed) - 1
        if remaining_empties:
            string += ' '.join('_' for _ in range(remaining_empties)) + '\n'

        return string


T = SplayTree()
T.add(13, 2)
T.add(2, 3)
T.add(4, 2)
T.add(5, 2)
print(T.string_representation(), end='')
print('a')

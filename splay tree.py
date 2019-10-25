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

    def search(self, key):
        node = self._search_node(key)
        if node is not None:
            return True
        else:
            return False

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

    def _previous(self, node: Node):
        if node.left_child is not None:
            return self._max_node(node.left_child)
        else:
            temp = node.parent
            while temp and node == temp.left_child:
                node = temp
                temp = temp.parent
            return temp

    def _next(self, node: Node):
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
            p_node = self._previous(node)
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

    def splay(self):
        pass


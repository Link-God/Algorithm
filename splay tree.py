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

    def _min_node(self):
        temp = self.root
        while temp.left_child:
            temp = temp.left_child
        return temp

    def _max_node(self):
        temp = self.root
        while temp.right_child:
            temp = temp.right_child
        return temp

    def min(self):
        node = self._min_node()
        return node.key, node.value

    def max(self):
        node = self._max_node()
        return node.key, node.value

    def delete(self, key):
        pass


class SplayTree(BST):
    def __init__(self):
        super().__init__()

    def splay(self):
        pass

    # def print(self):
    #     pass
    #
    # def set(self):
    #     pass
    #
    # def min(self):
    #     pass
    #
    # def max(self):
    #     pass
    #
    # def delete(self):
    #     pass
    #
    # def search(self):
    #     pass


T = BST()
print(T.max())
print(T.search(3))
T.add(3, 15)
print(T.max())
print(T)
T.add(1, 2)
T.add(4, 16)
print(T)
print(T.search(4))
print(T.search(3))
print(T.max())
print(T.min())

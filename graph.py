from collections import deque
import sys


class Vertex:

    def __init__(self, num, first_neighbor):
        self.neighbors = set()
        self.number = num
        self.flag = False
        self.add_neighbor(first_neighbor)

    def is_visited(self):
        self.flag = True

    def get_neighbors(self, reverse):
        # return self.neighbors
        return sorted(list(self.neighbors), reverse=reverse)

    def add_neighbor(self, new_neighbor):
        if new_neighbor is not None:
            self.neighbors.add(new_neighbor)


class Graph:
    vertices = {}

    def __init__(self, u_or_d, v, d_or_b):
        self.graph_type = u_or_d
        self.start_vertex = v
        self.type_graph_walk = d_or_b

    def print_graph(self):
        if self.type_graph_walk == 'd':
            self.deep_walk()
        elif self.type_graph_walk == 'b':
            self.width_walk()

    def add_vertex(self, num, neighbor):

        if self.vertices.get(num):
            self.vertices[num].add_neighbor(neighbor)
        else:
            self.vertices[num] = Vertex(num, neighbor)

        if self.graph_type == 'u':
            if self.vertices.get(neighbor):
                self.vertices[neighbor].add_neighbor(num)
            else:
                self.vertices[neighbor] = Vertex(neighbor, num)
        else:
            if self.vertices.get(neighbor):
                self.vertices[neighbor].add_neighbor(None)
            else:
                self.vertices[neighbor] = Vertex(neighbor, None)

    def deep_walk(self):
        deep_list = [self.vertices[self.start_vertex]]
        while len(deep_list):
            v = deep_list.pop()
            if not v.flag:
                print(v.number)
                v.is_visited()
                for i in v.get_neighbors(True):
                    if not self.vertices[i].flag:
                        deep_list.append(self.vertices[i])

    def width_walk(self):
        width_queue = deque([self.vertices[self.start_vertex], ])
        while len(width_queue):
            v = width_queue.popleft()
            if not v.flag:
                print(v.number)
                v.is_visited()
                for i in v.get_neighbors(False):
                    if not self.vertices[i].flag:
                        width_queue.append(self.vertices[i])


first_line = sys.stdin.readline().strip().split(' ')
g = Graph(*first_line)
for line in sys.stdin:
    if line == '\n':
        continue
    a, b = line.strip().split(' ')
    g.add_vertex(a, b)

g.print_graph()

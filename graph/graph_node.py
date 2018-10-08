class Node():
    def __init__(self, value):
        self.adjacent = []
        self.value = value

    def add_adjacent_nodes(self, node):
        self.adjacent.append(node)

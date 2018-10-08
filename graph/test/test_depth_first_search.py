import unittest
from graph.graph_node import Node
from graph.depth_first_search import depth_first_search


class DepthFirstSearch(unittest.TestCase):
    def test_empty_graph(self):
        graph = None
        self.assertEqual(depth_first_search(graph), {})

    def test_simple_graph(self):
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_1.add_adjacent_nodes(node_2)
        node_2.add_adjacent_nodes(node_3)
        depth_first = depth_first_search(node_1)
        self.assertEqual(depth_first, [node_1, node_2, node_3])

    def test_graph_with_cycle(self):
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_1.add_adjacent_nodes(node_2)
        node_2.add_adjacent_nodes(node_3)
        node_3.add_adjacent_nodes(node_1)
        depth_first = depth_first_search(node_1)
        self.assertEqual(depth_first, [node_1, node_2, node_3])

    def test_large_graph_with_cycle(self):
        node_0 = Node(0)
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_2.add_adjacent_nodes(node_0)
        node_2.add_adjacent_nodes(node_3)
        node_0.add_adjacent_nodes(node_1)
        node_0.add_adjacent_nodes(node_2)
        node_1.add_adjacent_nodes(node_2)
        node_3.add_adjacent_nodes(node_3)
        depth_first = depth_first_search(node_2)
        self.assertEqual(depth_first, [node_2, node_0, node_1, node_3])

    def test_larger_graph_with_cycle(self):
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(4)
        node_5 = Node(5)
        node_6 = Node(6)
        node_7 = Node(7)
        node_1.add_adjacent_nodes(node_2)
        node_1.add_adjacent_nodes(node_3)
        node_1.add_adjacent_nodes(node_4)
        node_2.add_adjacent_nodes(node_5)
        node_2.add_adjacent_nodes(node_6)
        node_3.add_adjacent_nodes(node_7)
        node_6.add_adjacent_nodes(node_4)
        depth_first = depth_first_search(node_1)
        self.assertEqual(depth_first, [node_1, node_2, node_5, node_6, node_4, node_3, node_7])

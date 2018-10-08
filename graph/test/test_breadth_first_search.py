import unittest
from graph.graph_node import Node
from graph.breadth_first_search import breadth_first_search


class BreadthFirstSearch(unittest.TestCase):
    def test_empty_graph(self):
        graph = None
        self.assertEqual(breadth_first_search(graph), {})

    def test_simple_graph(self):
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_1.add_adjacent_nodes(node_2)
        node_2.add_adjacent_nodes(node_3)
        breadth_first = breadth_first_search(node_1)
        self.assertEqual(breadth_first.get(0), [node_1])
        self.assertEqual(breadth_first.get(1), [node_2])
        self.assertEqual(breadth_first.get(2), [node_3])

    def test_graph_with_cycle(self):
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_1.add_adjacent_nodes(node_2)
        node_2.add_adjacent_nodes(node_3)
        node_3.add_adjacent_nodes(node_1)
        breadth_first = breadth_first_search(node_1)
        self.assertEqual(breadth_first.get(0), [node_1])
        self.assertEqual(breadth_first.get(1), [node_2])
        self.assertEqual(breadth_first.get(2), [node_3])

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
        breadth_first = breadth_first_search(node_2)
        self.assertEqual(breadth_first.get(0), [node_2])
        self.assertEqual(breadth_first.get(1), [node_0, node_3])
        self.assertEqual(breadth_first.get(2), [node_1])

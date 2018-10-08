import unittest
from graph.breadth_first_search import breadth_first_search


class BreadthFirstSearch(unittest.TestCase):
    def test_empty_graph(self):
        graph = None
        self.assertEqual(breadth_first_search(graph), [])

    def test_simple_graph(self):
        pass


    def test_graph_with_cycle(self):
        pass


    def test_large_graph_wit_cycle(self):
        pass
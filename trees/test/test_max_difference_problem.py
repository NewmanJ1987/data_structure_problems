import unittest
from trees.tree import Node
from trees.max_difference_problem import calc_max_diff


class MaxDifferenceProblem(unittest.TestCase):
    def test_full_tree(self):
        tree = Node(5, Node(1), Node(2))
        self.assertEqual(4, calc_max_diff(tree))

    def test_left_child_only(self):
        tree = Node(5, Node(1))
        self.assertEqual(4, calc_max_diff(tree))

    def test_right_child_only(self):
        tree = Node(5, None, Node(1))
        self.assertEqual(4, calc_max_diff(tree))


    def test_big_tree(self):
        left_subtree = Node(3, Node(4), Node(6))
        right_subtree = Node(1, Node(2), Node(5))
        tree = Node(10, left_subtree, right_subtree)
        self.assertEqual(9, calc_max_diff(tree))
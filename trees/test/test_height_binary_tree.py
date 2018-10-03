import unittest
from trees.tree import Node
from trees.height_binary_tree import height_complete_binary_tree, height_binary_tree


class CompleteBinaryTreeHeight(unittest.TestCase):
    def test_full_tree(self):
        tree = Node(2, Node(1), Node(5))
        height = height_complete_binary_tree(tree)
        self.assertEqual(height, 1)

    def test_big_tree(self):
        left_subtree = Node(3, Node(1), Node(4))
        right_subtree = Node(8, Node(7), Node(9))
        tree = Node(5, left_subtree, right_subtree)
        height = height_complete_binary_tree(tree)
        self.assertEqual(height, 2)

class BinaryTreeHeight(unittest.TestCase):
    def test_full_tree(self):
        tree = Node(2, Node(1), Node(5))
        height = height_binary_tree(tree)
        self.assertEqual(height, 1)

    def test_left_child_only(self):
        tree = Node(5, Node(1))
        height = height_binary_tree(tree)
        self.assertEqual(height, 1)

    def test_right_child_only(self):
        tree = Node(5, None, Node(9))
        height = height_binary_tree(tree)
        self.assertEqual(height, 1)

    def test_big_tree(self):
        left_subtree = Node(3, Node(1), Node(4))
        right_subtree = Node(8, Node(7), Node(9))
        tree = Node(5, left_subtree, right_subtree)
        height = height_binary_tree(tree)
        self.assertEqual(height, 2)
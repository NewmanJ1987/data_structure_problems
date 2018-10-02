import unittest
from trees.tree import Node
from trees.binary_search_tree_to_doubly_linked_list import create_linked_list


class MaxDifferenceProblem(unittest.TestCase):
    def test_full_tree(self):
        tree = Node(2, Node(1), Node(5))
        head = create_linked_list(tree)
        self.assertEqual(head.left, None)
        self.assertEqual(head.value, 1)
        self.assertEqual(head.right.value, 2)
        self.assertEqual(head.right.right.value, 5)

    def test_left_child_only(self):
        tree = Node(5, Node(1))
        head = create_linked_list(tree)
        self.assertEqual(head.left, None)
        self.assertEqual(head.value, 1)
        self.assertEqual(head.right.value, 5)

    def test_right_child_only(self):
        tree = Node(5, None, Node(9))
        head = create_linked_list(tree)

        self.assertEqual(head.left, None)
        self.assertEqual(head.value, 5)
        self.assertEqual(head.right.value, 9)

    def test_big_tree(self):
        left_subtree = Node(3, Node(1), Node(4))
        right_subtree = Node(8, Node(7), Node(9))
        tree = Node(5, left_subtree, right_subtree)
        head = create_linked_list(tree)
        self.assertEqual(head.left, None)
        self.assertEqual(head.value, 1)
        self.assertEqual(head.right.value, 3)
        self.assertEqual(head.right.right.value, 4)
        self.assertEqual(head.right.right.right.value, 5)
        self.assertEqual(head.right.right.right.right.value, 7)
        self.assertEqual(head.right.right.right.right.right.value, 8)
        self.assertEqual(head.right.right.right.right.right.right.value, 9)
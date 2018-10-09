import unittest
from trees.tree import RandomNode
from trees.clone_binary_tree_with_random_branch import clone_binary_tree, find_node_order


class CloneBinaryTreeRandomBranch(unittest.TestCase):
    def test_empty_tree(self):
        copy_tree = clone_binary_tree(None)
        self.assertEqual(copy_tree, None)

    def test_only_root(self):
        tree = RandomNode(2)
        copy_tree = clone_binary_tree(tree)
        self.assertEqual(tree.value, copy_tree.value)
        self.assertTrue(tree is not copy_tree)

    def test_clone_simple_tree(self):
        tree = RandomNode(2, RandomNode(1), RandomNode(3))
        copy_tree = clone_binary_tree(tree)
        self.assertEqual(tree.value, copy_tree.value)
        self.assertTrue(tree is not copy_tree)
        self.assertEqual(tree.left.value, copy_tree.left.value)
        self.assertTrue(tree.left is not copy_tree.left)
        self.assertEqual(tree.right.value, copy_tree.right.value)
        self.assertTrue(tree.right is not copy_tree.right)

    def test_clone_simple_tree_with_random(self):
        rand = RandomNode(3)
        with_rand = RandomNode(1, rand=rand)
        tree = RandomNode(2, with_rand, rand)
        copy_tree = clone_binary_tree(tree)
        self.assertEqual(tree.value, copy_tree.value)
        self.assertTrue(tree is not copy_tree)
        self.assertEqual(tree.left.value, copy_tree.left.value)
        self.assertTrue(tree.left is not copy_tree.left)
        self.assertEqual(tree.right.value, copy_tree.right.value)
        self.assertTrue(tree.right is not copy_tree.right)

    def test_clone_complex_tree_with_multiple_randoms(self):
        pass

    def test_find_node_order_one(self):
        to_find = RandomNode(1)
        tree = RandomNode(2, to_find, RandomNode(3))
        value, order = find_node_order(to_find, tree, 1)
        self.assertEqual(value, 1)
        self.assertEqual(order, 1)

    def test_find_node_order_many(self):
        to_find = RandomNode(1)
        tree = RandomNode(2, RandomNode(1, to_find), RandomNode(3))
        value, order = find_node_order(to_find, tree, 1)
        self.assertEqual(value, 1)
        self.assertEqual(order, 2)

# Note problem from
# https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem
import math


def height_complete_binary_tree(root):
    number_of_leaves = count_leaves(root, 0)
    return math.log(number_of_leaves, 2)


def count_leaves(node, count):
    if node.left:
        count = count_leaves(node.left, count)
    if node.right:
        count = count_leaves(node.right, count)
    if not node.left and not node.right:
        return count + 1
    return count


def height_binary_tree(root):
    pass

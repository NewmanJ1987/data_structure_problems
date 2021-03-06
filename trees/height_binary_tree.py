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


def height_binary_tree(node):
    if node.left:
        count_left = 1 + height_binary_tree(node.left)
    if node.right:
        count_right = 1 + height_binary_tree(node.right)
    if node.left and not node.right:
        return count_left
    if node.right and not node.left:
        return count_right
    if node.left and node.right:
        return max(count_left, count_right)
    return 0

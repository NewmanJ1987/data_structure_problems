#NOTE: Probelm from
# https://practice.geeksforgeeks.org/problems/maximum-difference-between-node-and-its-ancestor/1

def calc_max_diff(node):
    return traverse_tree(node, 0)


def traverse_tree(node, max_diff):
    if node.left:
        max_diff = calc_max_diff_in_subtree(max_diff, node.value, node.left)
        traverse_tree(node.left, max_diff)
    if node.right:
        max_diff = calc_max_diff_in_subtree(max_diff, node.value, node.right)
        traverse_tree(node.right, max_diff)
    return max_diff


def calc_max_diff_in_subtree(max_diff, value, node):
    difference = abs(node.value - value)
    if difference > max_diff:
        max_diff = difference
    if node.left:
        max_diff = calc_max_diff_in_subtree(max_diff, value, node.left)
    if node.right:
        max_diff = calc_max_diff_in_subtree(max_diff, value, node.right)
    return max_diff

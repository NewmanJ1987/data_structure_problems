from trees.tree import RandomNode


def clone_binary_tree(root):
    node_order_pairs = {}
    if root is None:
        return None
    if root:
        copy_root = copy_node(root, root, node_order_pairs)
    for node, (value, order_to_find) in node_order_pairs.items():
        node.rand = find_node(value, copy_root, 1, order_to_find)
    return copy_root


def copy_node(root, node, node_order_pairs):
    node_to_copy = None
    if node:
        node_to_copy = RandomNode(node.value)
    if node and node.left:
        node_to_copy.left = copy_node(root, node.left, node_order_pairs)
    if node and node.right:
        node_to_copy.right = copy_node(root, node.right, node_order_pairs)
    if node and node.rand:
        node_order_pairs.update({node_to_copy: find_node_order(node.rand, root, 1)})
    return node_to_copy


def find_node_order(node, tree, order):
    if node.value > tree.value:
        return find_node_order(node, tree.right, order)
    if node.value < tree.value:
        return find_node_order(node, tree.left, order)
    if node.value == tree.value and node is tree:
        return node.value, order
    return find_node_order(node, tree.left, order + 1)


def find_node(value, tree, order, order_to_find):
    if value > tree.value:
        return find_node(value, tree.right, order, order_to_find)
    if value < tree.value:
        return find_node(value, tree.left, order, order_to_find)
    if value == tree.value and order == order_to_find:
        return tree
    return find_node(value, tree.left, order + 1, order_to_find)

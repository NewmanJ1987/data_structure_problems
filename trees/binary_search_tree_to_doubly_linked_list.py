# Note: Problem from
# http://codercareer.blogspot.com/2011/09/interview-question-no-1-binary-search.html
def create_linked_list(root):
    traverse_tree(root)
    head = root
    while head.left:
        head = head.left
    return head


def find_biggest(node):
    if node.right:
        return find_biggest(node.right)
    return node


def find_lowest(node):
    if node.left:
        return find_lowest(node.left)
    return node


def traverse_tree(node):
    if node.left:
        node_left = find_biggest(node.left)
        traverse_tree(node.left)
        node_left.right = node
        node.left = node_left
    if node.right:
        node_right = find_lowest(node.right)
        traverse_tree(node.right)
        node_right.left = node
        node.right = node_right
    return node

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    @staticmethod
    def print_inorder(root):
        pass

    @staticmethod
    def print_preorder(root):
        pass

    @staticmethod
    def print_postorder(root):
        pass


class RandomNode(Node):
    def __init__(self, value, left=None, right=None, rand=None):
        super(RandomNode, self).__init__(value, left=left, right=right)
        self.rand = rand

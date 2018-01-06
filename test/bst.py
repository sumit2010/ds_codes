class BstIterator:
    def __init__(self, root):
        self.stack = []
        self.push(root)

    def next(self):
        node = self.stack.pop()
        self.push(node.right)
        return node

    def has_next(self):
        return len(self.stack) > 0

    def push(self, root):
        while root:
            self.stack.append(root)
            root = root.left


def inorder(root):
    inorder = []
    bst_iter = BstIterator(root)
    while bst_iter.has_next():
        inorder.append(bst_iter.next())
    return inorder
class BSTIterator:

    def __init__(self, root):
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        self.inorder = inorder(root)

    def next(self):
        return self.inorder.pop(0)

    def hasNext(self):
        return len(self.inorder) > 0


class BSTIteratorSol2:

    def __init__(self, root):
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        self.inorder = inorder(root)
        self.i = 0
        self.n = len(self.inorder)

    def next(self):
        node = self.inorder[self.i]
        self.i += 1
        return node

    def hasNext(self):
        return self.i < self.n


class BSTIteratorSol3:

    def __init__(self, root):
        self.stack = []
        self.curr = root

    def next(self):
        while self.curr:
            self.stack.append(self.curr)
            self.curr = self.curr.left

        node = self.stack.pop()
        self.curr = node.right
        return node.val

    def hasNext(self):
        return self.stack or self.curr


class BSTIteratorSol4:

    def __init__(self, root):

        self.generator = self.inorder_generator(root)
        self.curr = next(self.generator)

    def next(self) -> int:
        node = self.curr
        self.curr = self.next_node(self.generator)
        return node.val

    def hasNext(self) -> bool:
        return self.curr

    def next_node(self, generator):
        try:
            return next(generator)
        except StopIteration:
            return None

    def inorder_generator(self, node):
        if not node:
            return
        yield from self.inorder_generator(node.left)
        yield node
        yield from self.inorder_generator(node.right)
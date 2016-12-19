    def connect(self, root):
        if root is None:
            return
        levels = []
        def visit(node, depth):
            if node is None:
                return
            if len(levels)<depth:
                levels.append(node)
            else:
                levels[depth-1].next = node
                levels[depth-1] = node
            visit(node.left, depth+1)
            visit(node.right,depth+1)
        visit(root, 1)

class Solution(object):
    def hasPathSum(self, root, sum):
        def visit(node, cur):
            if not node: return False
            cur = cur+node.val
            if not(node.left) and not(node.right) and cur==sum: return True
            for ch in [node.left,node.right]:
                if visit(ch, cur): return True
            return False
        return visit(root, 0)

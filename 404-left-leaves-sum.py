class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        s = 0
        stack = [(root, False)]
        while len(stack)!=0:
            cur, leftie = stack.pop()
            if cur is None: continue
            if leftie and (cur.left is None) and (cur.right is None): s += cur.val
            stack.extend([(cur.right, False),(cur.left, True)])
        return s

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root is None:
            return []
        stack = [(root, 0)]
        while len(cur)!=0:
            cur, level = stack.pop()
            if len(res)==level:
                res.append([])
            res[level].append(cur.value)
            for e in (cur.left, cur.right):
                if not(e is None): stack.append((e, level+1))
        return res

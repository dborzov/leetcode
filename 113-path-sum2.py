class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        resp = []
        if not root:
            return resp
        stack = [(root, [root.val])]
        while len(stack)>0:
            cur, values = stack.pop()
            if not(cur.left) and not(cur.right) and (reduce(lambda x,y:x+y,values)==sum):
                resp.append(values[:])
            for ch in [cur.right, cur.left]:
                if not ch: continue
                stack.append( (ch, values + [ch.val] ) )
        return resp

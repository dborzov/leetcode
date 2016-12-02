# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        if not root:
            return
        self.rflatten(root)

    def rflatten(self, root):
        tail = root
        righto = root.right
        if root.left:
            ll_h, tail = self.rflatten(root.left)
            tail.right = righto
            root.right = ll_h
        if righto:
            rr_h, tail = self.rflatten(righto)
        root.left = None
        return root, tail

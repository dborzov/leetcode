class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        as_stack = lambda x:map(int, x.split('.'))
        stack1, stack2 = map(as_stack, (version1, version2))
        get_v = lambda l,idx: l[idx] if idx<len(l) else 0
        for i in range(max([len(stack1), len(stack2)])):
            v1 = get_v(stack1,i)
            v2 = get_v(stack2,i)
            if v1>v2: return 1
            if v2>v1: return -1
        return 0

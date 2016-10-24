class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k>n:
            return []
        def sub(cur,k):
            if k==1:
                return [[cur]]
            result = []
            for i in range(cur+1,n+1):
                for s in sub(i,k-1):
                    result.append([cur]+s)
            return result
        f = []
        for j in range(1,n+1):
            f += sub(j,k)
        return f
        

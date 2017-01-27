class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        stack = []
        for num in nums:
            if len(stack)==0:
                stack.append((num,num))
                continue
            low, high = stack[-1]
            if (high+1)==num:
                stack[-1] = (low, num)
            else:
                stack.append((num,num))
        return map(lambda x:str(x[0])+"->"+str(x[1]) if x[0]!=x[1] else str(x[0]),stack)

print Solution().summaryRanges([0,1,2,4,5,7])

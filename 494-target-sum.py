class Solution(object):
    def findTargetSumWays(self, nums, S):
        if abs(S)> sum(nums): return 0
        if S + sum(nums) % 2 ==1: return 0
        subsum = (S + sum(nums)) / 2
        counts = [1]+[0]*subsum
        for num in nums:
            for c in range(subsum,num-1,-1): counts[c] += counts[c-num]
        return counts[subsum]


print Solution().findTargetSumWays([1, 1, 1, 1, 1],300)

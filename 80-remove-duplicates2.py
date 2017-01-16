class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = {}
        offset = 0
        for idx, n in enumerate(nums):
            if counter.get(n,0)==2:
                offset += 1
                continue
            counter[n] = counter.get(n,0) + 1
            nums[idx-offset] = n
        return len(nums)-offset

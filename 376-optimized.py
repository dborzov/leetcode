from collections import namedtuple

class Solution(object):
    def wiggleMaxLength(self, nums):
        if len(nums)==0: return len(nums)
        length = 1
        last = nums[0]
        direction = None
        for el in nums[1:]:
            if (el > last) and (direction!='DOWN'):
                direction = 'DOWN'
                length += 1
            if (el < last) and (direction!='UP'):
                direction = 'UP'
                length += 1
            last = el
        return length

print Solution().wiggleMaxLength([1,1,2,3,4,5,6,7,8,7])

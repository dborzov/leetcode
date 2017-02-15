from collections import namedtuple

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0: return 0
        Lev = namedtuple('Lev',['v','len'])
        up, down = Lev(nums[0], 1), Lev(nums[0], 1)
        for el in nums[1:]:
            new_up, new_down = Lev(up.v, up.len), Lev(down.v, down.len)
            if (el > up.v):
                if (down.len < up.len+1) or ((down.len==up.len+1) and (el>down.v)):
                    new_down = Lev(el, up.len+1)
            if (el < down.v):
                if (up.len < down.len+1) or ((down.len+1==up.len) and (el<up.v)):
                    new_up = Lev(el, down.len+1)
            up, down = new_up, new_down
        return max(up.len, down.len)

print Solution().wiggleMaxLength([1,2,3,4,5,6,7,8,7])

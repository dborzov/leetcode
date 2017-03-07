class Solution(object):
    def searchInsert(self, nums, target):
        low, high = 0, len(nums)-1
        while (low <= high):
            mid = (low + high) // 2
            if nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
        return low

print Solution().searchInsert([1,3,5,6], 0)

class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        print nums
        closest_target = sum(nums[:3])
        for p1 in range(len(nums)-2):
            left, right = p1+1, len(nums)-1
            while (left < right):
                cur_sum = nums[p1] + nums[left] + nums[right]
                print 'at {},{},{} with {}'.format(nums[p1], nums[left], nums[right], closest_target)
                if abs(target - cur_sum) < abs(target - closest_target):
                    closest_target = cur_sum
                if cur_sum == target: return target
                if cur_sum > target:
                    right -= 1
                else:
                    left += 1
        return closest_target

print Solution().threeSumClosest([-1, 2, 1, -4], 1)

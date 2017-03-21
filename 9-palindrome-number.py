class Solution(object):
    def isPalindrome(self, x):
        val = str(x)
        for i in range(len(val)/2):
            if val[i] != val[-1-i]: return False
        return True


print Solution().isPalindrome(100)
print Solution().isPalindrome(121)
print Solution().isPalindrome(1911)
print Solution().isPalindrome(1991)
print Solution().isPalindrome(19791)
print Solution().isPalindrome(197091)

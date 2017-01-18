class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alphabetic = lambda f: (ord('a') <= ord(f.lower()) <= ord('z')) or (ord('0') <= ord(f.lower()) <= ord('9'))
        left = 0
        right = len(s)-1
        while True:
            while (left < right) and not alphabetic(s[left]):
                left += 1
            while (left < right) and not alphabetic(s[right]):
                right -= 1
            if left >= right:
                break
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

print Solution().isPalindrome("aa")

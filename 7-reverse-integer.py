class Solution(object):
    def reverse(self, x):
        minus = (x < 0)
        val = int(''.join(reversed([sym for sym in str(abs(x))])))
        if (val >= 2**31): return 0
        return -1*val if minus else val


print Solution().reverse(-123)

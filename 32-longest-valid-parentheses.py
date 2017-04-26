class Solution(object):
    def longestValidParentheses(self, s):
        def longest(s, key_sym):
            longest = 0
            idx_strike, cur_lev = 0, 0
            for idx, each in enumerate(s):
                cur_lev += -1 if each==key_sym else 1
                if cur_lev == 0:
                    # print "%s -%s- %s" % (s[:idx_strike], s[idx_strike:idx+1], s[idx+1:])
                    cur_len = (idx+ 1 - idx_strike)
                    if cur_len > longest: longest = cur_len
                if cur_lev > 0:
                    cur_lev = 0
                    idx_strike = idx + 1
            return longest
        return max(longest(reversed(s),')'), longest(s,'(') )

print Solution().longestValidParentheses('(((()(((((')


#     (  (   )  )  )
#   0  1  2  1   0  -1

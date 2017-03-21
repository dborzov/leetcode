class Solution(object):
    def isValid(self, s):
        closing = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        opening = set(closing.values())
        stack = []
        for each in s:
            if each in opening:
                stack.append(each)
                continue
            if each in closing:
                if (len(stack)==0) or (stack[-1] != closing[each]):
                    return False
                stack.pop()
        return len(stack)==0

print Solution().isValid('9[({(})])')

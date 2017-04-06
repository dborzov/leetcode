class Solution(object):
    def minWindow(self, s, t):
        min_ever = None
        counts = dict()
        for w in t:
            counts[w] = counts.get(w,0)+1
        cur = {'total': 0}
        left, right = 0,0
        while(right<len(s)):
            sym = s[right]
            if sym in counts:
                cur[sym] = cur.get(sym,0) + 1
                if cur[sym] <= counts[sym]:
                    cur['total'] += 1
            while (left < right):
                outcoming = s[left]
                if outcoming in counts:
                    if cur[outcoming] <= counts[outcoming]:
                        break
                    cur[outcoming] -= 1
                left += 1
            if cur['total']==len(t):
                print 'oh jee:',  min_ever
                if not(min_ever) or (len(min_ever) > (1+right - left)):
                    min_ever = s[left:right+1]
            right += 1
        return "" if not(min_ever) else min_ever

print 'hi'
print Solution().minWindow("A","A")

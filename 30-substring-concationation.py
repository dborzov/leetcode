class Solution(object):
  def findSubstring(self, s, words):
    if len(words)==0: return []
    l = len(words[0])
    shift_back = l*(len(words)-1)
    index = {}
    for w in words: index[w] = index.get(w,0) + 1
    results = []
    for shift in range(l):
        counter = index.copy()
        for idx in range(shift,len(s),l):
            prefix = s[idx:idx+l]
            phaseout = ''
            if idx-shift_back-l >= 0:
                phaseout = s[idx-shift_back-l:idx-shift_back]
                if phaseout in index:
                    counter[phaseout] = counter.get(phaseout,0) + 1
                    if counter[phaseout] == 0: del counter[phaseout]
            if not prefix in index:
                continue
            counter[prefix] = counter.get(prefix,0) - 1
            if counter[prefix] == 0: del counter[prefix]
            print 'prefix:', prefix,'phaseout:', phaseout, 'pos:  [', s[:idx],'*',s[idx:], ']  counter:', counter
            if len(counter)==0:
                results.append(s[idx-shift_back:idx+l])
    return results






print Solution().findSubstring("barfoothefoobarman", ["foo","bar"])

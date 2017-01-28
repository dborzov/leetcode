ii = ["eat", "tea", "tan", "ate", "nat", "bat"]

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sets = {}
        for w in strs:
            counter = [0]*26
            for ch in w: counter[ord(ch)-ord('a')] += 1
            key = ':'.join(str(x) for x in counter)
            if key in sets:
                sets[key].append(w)
            else:
                sets[key]=[w]
        return sorted([val for _, val in sets.items()], key=lambda x:-len(x))


print Solution().groupAnagrams(ii)

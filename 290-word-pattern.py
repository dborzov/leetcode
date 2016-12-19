class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        map_s2w = {}
        map_w2s = {}
        words = str.split()
        if len(words)==0 or (len(words) != len(pattern)): return False
        for idx, word in enumerate(words):
            sym = pattern[idx]
            if (sym in map_s2w) or (word in map_w2s):
                if (map_w2s.get(word) != sym) or (map_s2w.get(sym) != word):
                    return False
                continue
            map_s2w[sym]= word
            map_w2s[word]=sym
        return True

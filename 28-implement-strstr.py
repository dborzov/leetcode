def solution(haystack, needle):
        if len(needle)==0:
            return 0
        if len(needle)>len(haystack):
            return -1

        m = {}
        cur_repeats = needle[0]
        repeats = 1
        for i in range(1,len(needle)+1):
            if not(i==len(needle)) and (needle[i]==cur_repeats):
                repeats += 1
                continue
            key = cur_repeats + str(repeats)
            m[key] = m.get(key,[]) + [i - repeats]
            if i==len(needle):
                break
            cur_repeats = needle[i]
            repeats = 1


        match_cur = {}
        cur_repeats = haystack[0]
        repeats = 1
        for idx in range(1,len(haystack)+1):
            if not(idx==len(haystack)) and (haystack[idx]==cur_repeats):
                repeats += 1
                continue
            key = cur_repeats + str(repeats)
            new_cur = {}
            for pos in m.get(key,[]):
                if (pos==0) or (pos in match_cur):
                    if pos+repeats==len(needle):
                        return idx - len(needle)
                    new_cur[pos+repeats] = True
            match_cur = new_cur
            if len(haystack)==idx:
                break
            cur_repeats = haystack[idx]
            repeats = 1
        return -1
        if len(needle)==0:
            return 0
        if len(needle)>len(haystack):
            return -1

        m = {}
        cur_repeats = needle[0]
        repeats = 1
        for i in range(1,len(needle)+1):
            if not(i==len(needle)) and (needle[i]==cur_repeats):
                repeats += 1
                continue
            key = cur_repeats + str(repeats)
            m[key] = m.get(key,[]) + [i - repeats]
            if i==len(needle):
                break
            cur_repeats = needle[i]
            repeats = 1


        match_cur = {}
        cur_repeats = haystack[0]
        repeats = 1
        for idx in range(1,len(haystack)+1):
            if not(idx==len(haystack)) and (haystack[idx]==cur_repeats):
                repeats += 1
                continue
            key = cur_repeats + str(repeats)
            new_cur = {}
            for pos in m.get(key,[]):
                if (pos==0) or (pos in match_cur):
                    if pos+repeats==len(needle):
                        return idx - len(needle)
                    new_cur[pos+repeats] = True
            match_cur = new_cur
            if len(haystack)==idx:
                break
            cur_repeats = haystack[idx]
            repeats = 1
        return -1
        if len(needle)==0:
            return 0
        if len(needle)>len(haystack):
            return -1

        m = {}
        cur_repeats = needle[0]
        repeats = 1
        for i in range(1,len(needle)+1):
            if not(i==len(needle)) and (needle[i]==cur_repeats):
                repeats += 1
                continue
            key = cur_repeats + str(repeats)
            m[key] = m.get(key,[]) + [i - repeats]
            if i==len(needle):
                break
            cur_repeats = needle[i]
            repeats = 1


        match_cur = {}
        cur_repeats = haystack[0]
        repeats = 1
        for idx in range(1,len(haystack)+1):
            key = cur_repeats + str(repeats)
            if not(idx==len(haystack)) and (haystack[idx]==cur_repeats):
                repeats += 1
                continue
            new_cur = {}
            for pos in m.get(key,[]):
                if (pos==0) or (pos in match_cur):
                    if pos+repeats==len(needle):
                        return idx - len(needle)
                    new_cur[pos+repeats] = True
            match_cur = new_cur
            if len(haystack)==idx:
                break
            cur_repeats = haystack[idx]
            repeats = 1
        return -1

print solution("aaa", "a")

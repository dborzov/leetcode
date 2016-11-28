class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        def intify(low, high):
            return int(num[low:high])

        def match(ss, tp, level=0):
            if num[ss]=='0':
                return False
            sv = intify(ss, tp)
            print "  " * level + "- trying sum value: {} (depth:{})".format(sv, level)
            for rs in xrange(ss-1, -1, -1):
                rv = intify(rs, ss)
                if num[rs]=='0' and ((ss-rs)!=1):
                    print "  " * level + '- meh. see a zero-padded'
                    continue
                print "  " * level + "  -          right value: {}".format(rv)
                if rv>sv:
                    print "  " * level + "  -          woah, too big "
                    break
                lv = sv - rv
                if lv < 0:
                    continue
                lstr = len(str(lv))
                left_start = rs-lstr
                print "  " * level + "  -          expect left value: {}; see: \"{}\"".format(lv, num[min(0,left_start):rs])
                if left_start < 0:
                    continue
                lefter = intify(left_start,rs)
                if lefter!=lv:
                    continue
                if left_start==0:
                    print "  -          zing!"
                    return True
                else:
                    return match(rs, ss, level=level+1)
            return False



        for ss in range(len(num)-1, 0, -1):
            if match(ss, len(num),level=1):
                return True
        return False

Solution().isAdditiveNumber("121474836472147483648")

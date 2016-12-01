class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if (a < 0) and (b >= 0):
            return int(self.get_diff(b,-a))
        if (a >= 0) and (b < 0):
            return int(self.get_diff(a,-b))
        if (a<0) and (b<0):
            return int("-"+self.get_sum(-a,-b))
        return int(self.get_sum(a,b))


    def get_sum(self,a,b):
        astr = str(a)
        bstr = str(b)
        offset = 0
        result = ""
        for i in xrange(max(len(astr),len(bstr))):
            a_sym = int(astr[len(astr)-1-i]) if len(astr)-1-i>=0 else 0
            b_sym = int(bstr[len(bstr)-1-i]) if len(bstr)-1-i>=0 else 0
            print 'at {}: a_sym: {}, b_sym: {}'.format(i,a_sym,b_sym)
            tots = a_sym + b_sym + offset
            offset = 1 if tots >= 10 else 0
            result = str(tots % 10) + result
        return result

    def get_diff(self, a,b):
        if b>a:
            return '-'+self.get_diff(b,a)
        astr = str(a)
        bstr = str(b)
        offset = 0
        result = ""
        for i in xrange(max(len(astr),len(bstr))):
            a_sym = int(astr[len(astr)-1-i]) if len(astr)-1-i>=0 else 0
            b_sym = int(bstr[len(bstr)-1-i]) if len(bstr)-1-i>=0 else 0
            print 'at {}: a_sym: {}, b_sym: {}'.format(i,a_sym,b_sym)
            tots = a_sym  - offset - b_sym
            offset = 1 if tots < 0 else 0
            result = str(tots % 10) + result
        return result




print Solution().getSum(100,-22)

class Solution(object):
    def findRightInterval(self, intervals):
        starts = sorted(range(len(intervals)), key=lambda i:intervals[i].start)
        print 'sorted starts: ', starts
        results = []
        for iv in intervals:
            low, high = 0, len(intervals)-1
            while low <= high:
                mid = (low + high) // 2
                if iv.end > intervals[starts[mid]].start:
                    low = mid + 1
                else:
                    high = mid - 1
            results.append(-1 if low==len(intervals) else starts[low])
        return results

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

inputs = map(lambda x: Interval(*x), [ [1,4], [2,3], [3,4] ])
print Solution().findRightInterval(inputs)

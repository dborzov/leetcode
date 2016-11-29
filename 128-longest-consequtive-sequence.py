class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sets = []
        sizes = []
        pointers = {}
        def resolve(set_id):
            while (set_id != sets[set_id]):
                set_id = sets[set_id]
            return set_id

        for n in nums:
            if n in pointers:
                continue

            left = pointers.get(n-1, -1)
            right = pointers.get(n+1, -1)
            if (left==-1) and (right==-1):
                print "a new set for {}".format(n)
                set_id = len(sets)
                sets.append(set_id)
                sizes.append(1)
                pointers[n]=set_id
            elif (left == -1) or (right== -1):
                print "add {} to a neigbour".format(n)
                set_id = resolve(left + right + 1)
                sizes[set_id] += 1
                pointers[n] = set_id
            else:
                print "merging sets with {}".format(n)
                left_id =  resolve(left)
                right_id = resolve(right)
                sets[right_id]= left_id
                sizes[left_id] += sizes[right_id] + 1
                pointers[n] = right_id
            print 'sizes: ', sizes
            print 'sets : ', sets
        return max(sizes)






print Solution().longestConsecutive([1,3,5,2,4])

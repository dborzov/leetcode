class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        width = len(grid)
        if width==0:
            return 0
        height = len(grid[0])
        islands = []
        which_i = {}

        def key(i,j):
            return str(i)+","+str(j)

        def get(i,j):
            if (i<0) or (j<0):
                return False
            return grid[i][j]=='1'

        def resolve(cur):
            while (islands[cur]!=cur):
                cur = islands[cur]
            return cur

        for i in xrange(width):
            for j in xrange(height):
                if not get(i,j):
                    continue
                top, left  = get(i-1,j), get(i,j-1)
                if not(top) and not(left):
                    which_i[key(i,j)] = len(islands)
                    islands.append(len(islands))
                    continue
                if top != left:
                    island_id = which_i.get(key(i-1,j),0)+ which_i.get(key(i,j-1),0)
                    which_i[key(i,j)] = resolve(island_id)
                if top and left:
                    a, b = resolve(which_i[key(i-1,j)]), resolve(which_i[key(i,j-1)])
                    islands[b] = a
                    which_i[key(i,j)] = a

        import pdb; pdb.set_trace()
        cnt = 0
        for r in xrange(islands):
            if islands[r]==r: cnt+=1
        return cnt


Solution().numIslands(["11110","11010","11000","00000"])

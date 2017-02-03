class Solution(object):
    def PredictTheWinner(self, nums):
        if len(nums)==0: return False
        dp = [['*']*len(nums) for _ in range(len(nums))]
        turn = lambda x: 1-2*(x % 2)
        def assign(i,j):
            if (i+j)== len(nums)-1:
                return turn(i+j)*nums[i]
            down = dp[i+1][j]+turn(i+j)*nums[i]
            right = dp[i][j+1]+turn(i+j)*nums[-1-j]
            return max([down,right]) if turn(i+j)==1 else min([down,right])
        for lev in range(len(nums)-1,-1,-1):
            for d in range(lev+1):
                dp[lev-d][d] = assign(lev-d,d)
        return dp[0][0]>=0

print Solution().PredictTheWinner([60,80,10])

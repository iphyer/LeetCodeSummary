class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:       
        dp = [ [0 for _ in range(n+1)] for _ in range(m+1) ]
        # dp[i][j]: max number of elements with i's 0 and j's 1
        # for a str of zeros and ones
        # dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones]+1)
        
        for s in strs:
            zeros = s.count('0')
            ones  = s.count('1')
            for i in range(m, zeros-1, -1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones]+1)
        return dp[m][n]

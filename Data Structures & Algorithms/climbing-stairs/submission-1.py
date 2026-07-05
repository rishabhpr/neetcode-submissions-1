class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0: 1, -1: 0}
        def dfs(remaining):
            if remaining in memo:
                return memo[remaining]

            else:
                memo[remaining] = dfs(remaining-1) + dfs(remaining-2)
                return memo[remaining]

        
        dfs(n)
        return memo[n]
        
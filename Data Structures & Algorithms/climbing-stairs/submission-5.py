class Solution:
    def climbStairs(self, n: int) -> int:
        prev2 = 1
        prev1 = 1
        cur = 1

        for i in range(2, n+1):
            cur = prev2 + prev1
            prev2 = prev1
            prev1 = cur
        
        return cur

        
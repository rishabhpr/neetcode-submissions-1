class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(start, remaining):
            if remaining == 0:
                res.append(path.copy())
                return
            
            if remaining <0:
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i,remaining - nums[i])
                path.pop()
        
        dfs(0,target)
        return res
        
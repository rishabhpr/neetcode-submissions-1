class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def backtrack(i):
            if i == len(nums):
                res.append(path.copy())
                return

            # we are at ith index
            #select i
            path.append(nums[i])
            backtrack(i+1)
            path.pop()
            backtrack(i+1)

            return
        
        backtrack(0)
        return res


        
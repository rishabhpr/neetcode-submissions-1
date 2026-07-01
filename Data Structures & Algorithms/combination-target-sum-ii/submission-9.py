class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        path = []
        candidates.sort()

        def backtrack(start, remaining):
            if remaining == 0:
                res.append(path.copy())
                return
            
            for i in range(start, len(candidates)):
                if i>start and candidates[i] == candidates[i-1]:
                    continue
                if remaining < candidates[i]:
                    continue
                path.append(candidates[i])
                backtrack(i+1, remaining - candidates[i])
                path.pop()
            
        
        backtrack(0, target)
        return res

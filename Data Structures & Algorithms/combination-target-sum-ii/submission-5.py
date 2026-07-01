class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        path = []
        candidates.sort()

        def backtrack(start, remaining):
            if remaining == 0:
                res.append(path.copy())
                return
            
            if remaining <0: 
                return
            
            for i in range(start, len(candidates)):
                candidate = candidates[i]
                if i>start and candidate == candidates[i-1]:
                    continue
                path.append(candidate)
                backtrack(i+1, remaining - candidate)
                path.pop()
            
        
        backtrack(0, target)
        return res

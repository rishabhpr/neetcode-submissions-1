class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:


        intervals.sort(key = lambda x: x[0])

        merged = []

        for start, end in intervals:
            if len(merged) == 0:
                merged.append([start,end])
            elif start <= merged[-1][1]:
                merged[-1][1] = max(end, merged[-1][1])
            else:
                merged.append([start, end])
        
        return merged
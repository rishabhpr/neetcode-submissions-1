class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        new_start = newInterval[0]
        new_end = newInterval[1]
        for i in range(len(intervals)):
            interval = intervals[i]
            start = interval[0]
            end = interval[1]

            # interval before newInterval
            if end < new_start:
                res.append(interval)
                continue
            
            # interval after newInterval
            if start > new_end:
                res.append([new_start, new_end])
                res.extend(intervals[i:])
                return res

            # overlap
            new_start = min(new_start,start)
            new_end = max(new_end,end)

        res.append([new_start,new_end])
        return res
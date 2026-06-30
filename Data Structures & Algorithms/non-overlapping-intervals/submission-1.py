class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        remove_count = 0

        if len(intervals) <=1 :
            return 0

        sorted_intervals = sorted(intervals, key = lambda x: x[0])

        prev_end = sorted_intervals[0][1]
        for i in range(1, len(sorted_intervals)):

            start = sorted_intervals[i][0]
            end = sorted_intervals[i][1]

            if prev_end > start:
                # overlapping
                remove_count+=1
                prev_end = min(prev_end, end)
            else:
                prev_end = end
            
        
        return remove_count
            



        
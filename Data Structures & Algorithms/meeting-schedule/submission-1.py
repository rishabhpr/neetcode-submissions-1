"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_interval = sorted(intervals, key=lambda x: x.start)

        for i in range(1, len(sorted_interval)):
            prev_end = sorted_interval[i-1].end
            start =  sorted_interval[i].start

            if prev_end > start:
                return False
        
        return True

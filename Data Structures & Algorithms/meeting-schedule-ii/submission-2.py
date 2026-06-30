"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        sorted_intervals = sorted(intervals, key = lambda x: x.start)

        heap = []
        rooms = 0

        for i in range(len(sorted_intervals)):
            cur_start = sorted_intervals[i].start

            # check if any exisitng room can be used
            if heap and heap[0] <= cur_start:
                heapq.heappop(heap)
                heapq.heappush(heap, sorted_intervals[i].end)
            else:
                heapq.heappush(heap, sorted_intervals[i].end)
            
            rooms = max(rooms, len(heap))
        

        return rooms



        
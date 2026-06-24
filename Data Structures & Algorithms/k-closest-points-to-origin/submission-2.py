class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            dist = x*x + y*y
            heapq.heappush(heap, (dist,x,y))
        
        result = []
        for i in range(k):
            point = heapq.heappop(heap)[1:]
            result.append(list(point))
        
        return result
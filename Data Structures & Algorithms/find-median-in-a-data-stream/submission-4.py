class MedianFinder:

    def __init__(self):
        self.small = [] #max-heap
        self.large = []

    def addNum(self, num: int) -> None:

        heapq.heappush(self.small, -num)

        x = - heapq.heappop(self.small)
        heapq.heappush(self.large, x)

        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        
        return float(-self.small[0] + self.large[0]) / 2 
        
        
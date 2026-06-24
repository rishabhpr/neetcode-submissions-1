class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        queue = deque()
        heap = [-freq for freq in count.values()]
        heapq.heapify(heap)
        time = 0

        while heap or queue:
            time +=1

            if queue:
                if queue[0][1] <= time:
                    heapq.heappush(heap, queue.popleft()[0])

            if heap:
                cur = heapq.heappop(heap)
                cur +=1
            
                if cur !=0:
                    queue.append((cur, time + n+1))
        
        return time

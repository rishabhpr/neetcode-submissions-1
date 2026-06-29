class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        answer = right

        def can_finish(speed):
            total_hours = 0
            for num in piles:
                total_hours += math.ceil(num / speed)
            return total_hours <= h

        while left <= right:
            mid = (left + right) // 2

            if can_finish(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer

        
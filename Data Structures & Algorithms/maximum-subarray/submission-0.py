class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = nums[0]
        best_sum = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            cur_sum = max(num, cur_sum + num )
            best_sum = max(best_sum, cur_sum)

        
        return best_sum
        
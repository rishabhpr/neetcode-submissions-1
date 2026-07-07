class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for i in range(len(nums)):
            num = nums[i]
            if target-num in nums_map:
                return [nums_map[target-num], i]
            else:
                nums_map[num] = i
    
    
        




        
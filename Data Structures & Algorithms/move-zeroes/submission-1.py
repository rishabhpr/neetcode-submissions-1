class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 0

        # left tracks the first zero element
        # right scans the window

        while right < len(nums):
            if nums[right] != 0:
                #swap with left
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            

            right+=1


        
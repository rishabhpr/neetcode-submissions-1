class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left+right) // 2

            if nums[mid] == target:
                return mid
            
            # left side sorted
            if nums[left] <= nums[mid]:
                #check if taregt in left half
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            
            #right side sorted
            elif nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        
        return -1



        
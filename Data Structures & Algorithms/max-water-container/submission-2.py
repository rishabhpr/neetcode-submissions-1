class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        left = 0
        right = len(heights)-1

        while(left<right):
            cur_water = min(heights[left], heights[right]) * (right-left)
            max_water = max(cur_water,max_water)
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        
        return max_water


        
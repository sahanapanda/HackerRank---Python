class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            # Calculate the current width and height
            width = right - left
            current_height = min(height[left], height[right])
            
            # Calculate current area and update the maximum
            current_water = width * current_height
            max_water = max(max_water, current_water)
            
            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Sort the array to use the two-pointer technique
        nums.sort()
        n = len(nums)
        
        # Initialize the closest sum with the sum of the first three elements
        closest_sum = nums[0] + nums[1] + nums[2]
        
        # Iterate through the array, fixing the first element of the triplet
        for i in range(n - 2):
            # Optional optimization: Skip duplicate values for the fixed element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If we find the exact target, return it immediately
                if current_sum == target:
                    return current_sum
                
                # Update closest_sum if the current_sum is closer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers based on the comparison with target
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum

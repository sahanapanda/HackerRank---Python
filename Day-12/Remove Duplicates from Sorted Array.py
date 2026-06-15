class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # Pointer to place the next unique elements
        write_index = 1
        
        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # If the current element is different from the previous element, it's unique
            if nums[i] != nums[i - 1]:
                nums[write_index] = nums[i]
                write_index += 1
                
        # write_index represents the count of unique elements
        return write_index
        

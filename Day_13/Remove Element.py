class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Pointer to place the next element that is not equal to val
        k = 0
        
        # Iterate through the array with a fast pointer
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
                
        # k represents the number of elements not equal to val
        return k

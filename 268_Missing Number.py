class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        
        i = 0
        while i < len(nums):
            if nums[i] != i:
                return i
            else: 
                i += 1
        return i
            
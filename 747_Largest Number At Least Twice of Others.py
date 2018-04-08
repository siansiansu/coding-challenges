class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        nums_copy = nums[:]
        nums.sort()
        if nums[-1] >= nums[-2] * 2:
            return nums_copy.index(nums[-1])
        else:
            return -1

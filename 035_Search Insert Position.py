class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n == 0 or target <= nums[0]:
            return 0
        if target > nums[n - 1]:
            return n
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        if target > nums[left]:
            return left + 1
        else:
            return left

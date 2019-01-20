class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums2 = nums[:]

        for i in range(len(nums2)):
            nums[(i + k) % len(nums)] = nums2[i]
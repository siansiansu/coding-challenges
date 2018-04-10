class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_sort = sorted(nums)
        s = e = -1
        for i in range(len(nums)):
            if nums[i] != nums_sort[i]:
                if s == -1:
                    s = i
                e = i
        return e - s + 1 if e != s else 0

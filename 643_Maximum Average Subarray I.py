class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        base = sum(nums[:k])
        tmp = base
        for i in range(len(nums) - k):
            tmp = tmp - nums[i] + nums[i + k]
            base = max(base, tmp)
        return float(base) / float(k)

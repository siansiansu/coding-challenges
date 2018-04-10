class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0: return 0
        c = collections.Counter(nums)
        return sum(c[n + k] > 1 - bool(k) for n in c.keys())
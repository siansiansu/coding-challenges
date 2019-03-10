class Solution:
    def twoSum(self, nums, target):
        dict = {}
        for i, j in enumerate(nums):
            if target - j in dict:
                return [dict[target - j], i]
            dict[j] = i

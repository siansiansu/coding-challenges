#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#%%
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current = 0
        maxsum = -9**99

        for i in range(len(nums)):
            if current < 0: current = 0
            current += nums[i]
            maxsum = max(maxsum, current)
        return maxsum
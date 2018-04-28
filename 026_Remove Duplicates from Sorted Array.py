#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        count = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[count]:
                count += 1
                nums[count] = nums[i]
        return count + 1


if __name__ == "__main__":
    print(Solution().removeDuplicates([1, 1, 1, 1, 2, 2, 3, 3]))

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        start = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[start]:
                start += 1
                nums[start] = nums[i]
        return start + 1


if __name__ == "__main__":
    print(Solution().removeDuplicates([1, 1, 1, 1, 2, 2, 3, 3]))

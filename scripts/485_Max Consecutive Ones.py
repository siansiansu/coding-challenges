class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = count = 0
        for i in nums:
            if i == 1:
                count += 1
                ans = max(ans, count)
            else:
                count = 0
        return ans


if __name__ == "__main__":
    print(Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))

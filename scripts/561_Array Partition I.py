class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(nums[::2])
    
if __name__ == "__main__":    
    print(Solution().arrayPairSum([1, 4, 3, 2]))
    

class Solution:
    def arrayPairSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        results = []
        for i in range(0, len(nums), 2):
            mini = min(nums[i], nums[i + 1])
            results.append(mini)
        return sum(results)


if __name__ == "__main__":
    print(Solution().arrayPairSum2([1, 4, 3, 2]))




class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = set(nums)
        if len(num) < 3:
            return max(num)
        num.remove(max(num))
        num.remove(max(num))
        return max(num)
    
if __name__ == "__main__":    
    print(Solution().thirdMax([2,2,3,4,5,6,7]))  
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums == 0: 
            return ''
        elif val not in nums:
            return len(nums)
        else:
            while val in nums:
                nums.remove(val)
        return len(nums)
        
if __name__ == "__main__":   
    print(Solution().removeElement([2,2,3,3,3], [3]))
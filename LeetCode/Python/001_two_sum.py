class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = dict()
        for index, num in enumerate(nums):
            if target - num in hash_table:
                return [hash_table[target - num], index]
                break
            hash_table[num] = index
            
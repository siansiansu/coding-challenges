class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        h = len(nums)
        w = len(nums[0])

        if h * w != r * c:
            return nums

        ans = []
        p = q = 0
        for i in range(r):
            row = []
            for j in range(c):
                row.append(nums[p][q])
                q += 1
                if q == w:
                    p += 1
                    q = 0
            ans.append(row)
        return ans


if __name__ == "__main__":
    nums = [[1, 2], [3, 4], [5, 6]]
    r = 2
    c = 3
    print(Solution().matrixReshape(nums, r, c))

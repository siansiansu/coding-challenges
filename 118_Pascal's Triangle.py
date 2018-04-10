class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        res = [[1]]
        for i in range(1, numRows):
            res.append([])
            for j in range(i + 1):
                res[i].append((res[i - 1][j - 1] if j > 0 else 0) +
                              (res[i - 1][j] if j < i else 0))
        return res

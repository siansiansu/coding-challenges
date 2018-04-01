class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum(s in J for s in S)


if __name__ == "__main__":
    print(Solution().numJewelsInStones("aA", "aAAaAAbbbb"))

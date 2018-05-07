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



class Solution:
    def numJewelsInStones2(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        answer = 0
        for i in J:
            for j in S:
                if i == j:
                    answer += 1
        return answer


if __name__ == "__main__":
    print(Solution().numJewelsInStones2("aA", "aAAaAAbbbb"))
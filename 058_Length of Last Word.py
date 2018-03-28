class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.rstrip().split(' ')[-1])

if __name__ == "__main__":    
    print(Solution().lengthOfLastWord('Hello World'))   
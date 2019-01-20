class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        return len(A) == len(B) and A in (B + B)

if __name__ == "__main__":    
    print(Solution().rotateString('abcde', 'abced'))
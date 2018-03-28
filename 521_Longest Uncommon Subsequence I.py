class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a != b: 
            return max(len(a), len(b))
        else: 
            return -1 
    
if __name__ == "__main__":    
    print(Solution().findLUSlength('aba', 'cdc'))
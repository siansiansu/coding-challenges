class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        cntDict = collections.Counter(magazine)
        for letter in ransomNote:
            cntDict[letter] -= 1
            if cntDict[letter]<0: 
                return False
        return True
    
if __name__ == "__main__":    
    print(Solution().canConstruct("aa", "aab"))  
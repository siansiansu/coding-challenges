class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """     
        if not strs: return ''  
        for seq, numStrs in enumerate(zip(*strs)):
            if len(set(numStrs)) > 1:
                return strs[0][:seq]
        return min(strs)
    
if __name__ == "__main__":   
    print(Solution().longestCommonPrefix(['abde', 'ab', 'ab']))
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        
        res = ""
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i > len(strs[j]) or strs[j][i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    strs2 = ["dog","racecar","car"]
    print(Solution().longestCommonPrefix(strs))

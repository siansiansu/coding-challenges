#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def longestCommonPrefix1(self, strs):
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

    def longestCommonPrefix2(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ''
        strs.sort()
        res = ''
        for ix in range(len(strs[0])):
            if ix >= len(strs[-1]) or strs[-1][ix] != strs[0][ix]:
                return res
            res += strs[0][ix]
        return res


    def longestCommonPrefix3(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ''

        for i, j in enumerate(zip(*strs)):
            if len(set(j)) > 1:
                return strs[0][:i]
        return min(strs)


if __name__ == "__main__":
    strs = ["flower","flow","flight"] 
    print(Solution().longestCommonPrefix1(strs))
    print(Solution().longestCommonPrefix2(strs))
    print(Solution().longestCommonPrefix3(strs))

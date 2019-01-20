#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        for i, j in enumerate(zip(*strs)):
            if len(set(j)) > 1:
                return strs[0][:i]
        return min(strs)


if __name__ == "__main__":
    print(Solution().longestCommonPrefix(['abde', 'ab', 'ab']))




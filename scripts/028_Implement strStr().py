#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)

if __name__ == "__main__":
    haystack = 'hello'
    needle = 'll'
    print(Solution().strStr(haystack, needle))


class Solution(object):
    def strStr2(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1


if __name__ == "__main__":
    haystack = 'hello'
    needle = 'll'
    print(Solution().strStr2(haystack, needle))